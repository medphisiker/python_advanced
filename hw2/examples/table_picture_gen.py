from latex_gen_small import latex_gen_small as tex_gen


if __name__ == "__main__":
    data = [
        ["Header 1", "Header 2", "Header 3"],
        ["Data 1", "Data 2", "Data 3"],
        ["Data 4", "Data 5", "Data 6"],
    ]

    image_name = "mesh"

    latex_code_table = tex_gen.create_latex_table(data)
    latex_code_image = tex_gen.create_latex_image(image_name)

    latex_code = latex_code_table, latex_code_image
    latex_code = tex_gen.latex_code_union(latex_code)

    latex_code = tex_gen.make_latex_document(latex_code)
    tex_gen.write_to_file(latex_code, "main_table_picture.tex")
