import idc
import hashlib
import idaapi

admin_func = [
    "add_node",
    "remove_node",
    "get_best_fit",
    "get_last_node",
    "init_heap",
    "heap_alloc",
    "heap_free",
    "expand",
    "contract",
    "get_bin_index",
    "create_foot",
    "get_foot",
    "get_wilderness",
    "tiny_mmap",
    "tiny_munmap",
    "tiny_execve",
    "admin_menu",
    "admin_showstate",
    "admin_showgameboard",
    "admin_game",
    "admin_set_seed",
    "my_heap_alloc",
    "my_heap_free",
    "show",
    "edit",
    "allocate",
    "delete",
    "heap_init",
    "unmap_all",
    "clean1",
    "clean2",
    "map_all_file",
]


def get_func_args(ea):
    d_res = idaapi.decompile(ea)
    line = str(d_res).splitlines()[0]
    if "()" in line:
        return 0
    return line.count(",") + 1

def find_segm_byname(target_name):
    for ea in Segments():
        name = idc.get_segm_name(ea)
        if target_name == name:
            return ea

def calac_name_hash(content):
    content += "_HHHHHHHHHashhhhhhhh"
    md5hash = hashlib.md5(content.encode())
    md5 = md5hash.hexdigest()
    # print(md5)
    md5_array = ", ".join([hex(i) for i in md5hash.digest()[::-1]])
    return md5, md5_array

def dump_to_output(start, end, name):
    func_hex, func_hexarr = calac_name_hash(name)
    content = idc.get_bytes(start, end-start)
    with open(f"admin_output/{func_hex}", "wb") as f:
        f.write(content)
    if name not in admin_func:
        with open(f"output/{func_hex}", "wb") as f:
            f.write(content)
    print(f"{hex(start)}\t{name}\t{func_hex}\t{func_hexarr}")

    # arg_num = get_func_args(start)
    # argsl = ", ".join([f"arg{i}" for i in range(arg_num)])
    # print("#ifdef FUNCTION_PROXY")
    # print("#define FUNCTION_%s(%s) ({ \\" % (name, argsl))
    # print("register __m128i exid_in_%s asm(\"xmm15\"); \\" % name)
    # print(f"exid_in_{name} = _mm_set_epi8({func_hexarr}); \\")
    # print(f"FUNCTION_ARG{arg_num}({argsl}); \\")
    # print("})")
    # print("#else")
    # print("#define FUNCTION_%s  %s" % (name, name))
    # print("#endif")
    # print()

def dump_all_functions():
    text_segm = find_segm_byname(".text")
    text_start = idc.get_segm_start(text_segm)
    text_end = idc.get_segm_end(text_segm)

    for ea in Functions():
        if text_start <= ea  <= text_end:
            func_name = idc.get_name(ea)
            func_end = find_func_end(ea)
            dump_to_output(ea, func_end, func_name)
            # print(func_name)
            
idc.auto_wait()
print("1231231")
dump_all_functions()

ida_pro.qexit(0)