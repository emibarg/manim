import manim as mn
from manim import Tex


class RelationalAlgebra(mn.Scene):
    def construct(self):
        ## Title Card
        title = mn.Text("Algebra Relacional", font_size=60)
        self.play(mn.Write(title))
        self.wait(2)
        self.play(mn.FadeOut(title))

        queEs = mn.Text("¿Qué es el algebra relacional?", font_size=60)
        self.play(mn.Write(queEs))
        self.wait(2)
        self.play(mn.FadeOut(queEs))

        ## Slide 1
        top_left_text = mn.Text(
            "An: Atributo 'n'\n \n Tn: Tupla 'n' \n \n Vn: Valor 'n'", font_size=30
        )
        top_left_text.to_corner(mn.UL).shift(0.5 * mn.LEFT)
        self.play(mn.Write(top_left_text))
        self.wait(2)
        ##Table

        table = mn.Table(
            [["V1", "V2"], ["V1", "V2"]],
            row_labels=[mn.Text("T1", color=mn.PURPLE), mn.Text("T2", color=mn.PURPLE)],
            col_labels=[mn.Text("A1", color=mn.RED), mn.Text("A2", color=mn.RED)],
            top_left_entry=mn.Star(color=mn.YELLOW).scale(0.3),
            include_outer_lines=True,
            line_config={"stroke_width": 1, "color": mn.YELLOW},
        )

        self.play(mn.Write(table))
        self.wait(2)

        # Highlight the col labels
        highlight_col_label_1 = table.get_highlighted_cell((1, 2), color=mn.GREEN)
        highlight_col_label_2 = table.get_highlighted_cell((1, 3), color=mn.GREEN)
        self.add(
            highlight_col_label_1, highlight_col_label_2
        )  # Add the highlighted cell to the scene
        self.play(
            mn.FadeIn(highlight_col_label_1), mn.FadeIn(highlight_col_label_2)
        )  # Fade in the highlighted cell

        self.wait(2)
        self.play(mn.FadeOut(highlight_col_label_1), mn.FadeOut(highlight_col_label_2))

        self.wait(2)

        # highlight the row labels
        highlight_row_label_1 = table.get_highlighted_cell((2, 1), color=mn.GREEN)
        highlight_row_label_2 = table.get_highlighted_cell((3, 1), color=mn.GREEN)
        self.add(highlight_row_label_1, highlight_row_label_2)
        self.play(mn.FadeIn(highlight_row_label_1), mn.FadeIn(highlight_row_label_2))

        self.wait(2)
        self.play(mn.FadeOut(highlight_row_label_1), mn.FadeOut(highlight_row_label_2))

        self.wait(2)

        # highlight each value in succession
        highlight_value_1 = table.get_highlighted_cell((2, 2), color=mn.GREEN)
        highlight_value_2 = table.get_highlighted_cell((2, 3), color=mn.GREEN)
        highlight_value_3 = table.get_highlighted_cell((3, 2), color=mn.GREEN)
        highlight_value_4 = table.get_highlighted_cell((3, 3), color=mn.GREEN)

        self.play(mn.FadeIn(highlight_value_1))
        self.play(mn.FadeIn(highlight_value_2))
        self.play(mn.FadeIn(highlight_value_3))
        self.play(mn.FadeIn(highlight_value_4))

        self.wait(2)

        self.play(
            mn.FadeOut(highlight_value_1),
            mn.FadeOut(highlight_value_2),
            mn.FadeOut(highlight_value_3),
            mn.FadeOut(highlight_value_4),
        )

        self.wait(5)

        ## Table with actual example

        table2 = mn.Table(
            [["Peter", "Parker"], ["Clark", "Kent"]],
            row_labels=[mn.Text("1", color=mn.PURPLE), mn.Text("2", color=mn.PURPLE)],
            col_labels=[
                mn.Text("Nombre", color=mn.RED),
                mn.Text("Apellido", color=mn.RED),
            ],
            include_outer_lines=True,
            line_config={"stroke_width": 1, "color": mn.YELLOW},
        )

        self.play(mn.FadeOut(top_left_text), mn.Transform(table, table2))

        self.wait(5)
        ##nuevamente resaltamos columnas
        highlight_col_label_1 = table2.get_highlighted_cell((1, 2), color=mn.GREEN)
        highlight_col_label_2 = table2.get_highlighted_cell((1, 3), color=mn.GREEN)
        self.add(highlight_col_label_1, highlight_col_label_2)
        self.play(mn.FadeIn(highlight_col_label_1), mn.FadeIn(highlight_col_label_2))

        self.wait(2)

        self.play(mn.FadeOut(highlight_col_label_1), mn.FadeOut(highlight_col_label_2))

        self.wait(2)
        ##nuevamente resaltamos filas
        highlight_row_label_1 = table2.get_highlighted_cell((2, 1), color=mn.GREEN)
        highlight_row_label_2 = table2.get_highlighted_cell((3, 1), color=mn.GREEN)
        self.add(highlight_row_label_1, highlight_row_label_2)
        self.play(mn.FadeIn(highlight_row_label_1), mn.FadeIn(highlight_row_label_2))

        self.wait(2)

        self.play(mn.FadeOut(highlight_row_label_1), mn.FadeOut(highlight_row_label_2))

        self.wait(2)

        ##nuevamente resaltamos valores

        highlight_value_1 = table2.get_highlighted_cell((2, 2), color=mn.GREEN)
        highlight_value_2 = table2.get_highlighted_cell((2, 3), color=mn.GREEN)
        highlight_value_3 = table2.get_highlighted_cell((3, 2), color=mn.GREEN)
        highlight_value_4 = table2.get_highlighted_cell((3, 3), color=mn.GREEN)

        self.play(mn.FadeIn(highlight_value_1))
        self.play(mn.FadeIn(highlight_value_2))
        self.play(mn.FadeIn(highlight_value_3))
        self.play(mn.FadeIn(highlight_value_4))

        self.wait(2)

        self.play(
            mn.FadeOut(highlight_value_1),
            mn.FadeOut(highlight_value_2),
            mn.FadeOut(highlight_value_3),
            mn.FadeOut(highlight_value_4),
        )

        self.wait(5)

        ##resaltamos dominio

        TextoDominio = mn.Text(
            "Dominio: Conjunto de valores que puede tomar un atributo", font_size=30
        )
        TextoDominio.to_corner(mn.UL).shift(0.5 * mn.LEFT)
        self.play(mn.Write(TextoDominio))

        self.wait(5)

        textoD1 = mn.Text("D1 = {Peter, Clark}", font_size=30)
        textoD2 = mn.Text("D2 = {Parker, Kent}", font_size=30)

        textoD1.next_to(TextoDominio, mn.DOWN)
        textoD2.next_to(TextoDominio, mn.DOWN)

        self.play(mn.Write(textoD1))

        self.play(mn.FadeIn(highlight_value_1), mn.FadeIn(highlight_value_3))
        self.wait(2)
        self.play(mn.FadeOut(highlight_value_1), mn.FadeOut(highlight_value_3))
        self.play(mn.Transform(textoD1, textoD2))
        self.play(mn.FadeIn(highlight_value_2), mn.FadeIn(highlight_value_4))
        self.wait(2)
        self.play(mn.FadeOut(highlight_value_2), mn.FadeOut(highlight_value_4))
        self.wait(5)

        self.play(mn.FadeOut(TextoDominio), mn.FadeOut(textoD1), mn.FadeOut(textoD2))

        self.wait(3)

        Subconjunto = mn.Tex(
            r"La relación nombre apellido es un subconjunto de: $\{D1\} \times \{D2\}$",
            font_size=40,
        )

        Subconjunto.to_corner(mn.UL)

        self.play(mn.Write(Subconjunto))

        self.wait(2)

        self.play(mn.FadeOut(table, table2, Subconjunto))

        self.wait(2)

        ##Definicion Formal
        title2 = mn.Text("Definición Formal", font_size=45)
        title2.to_corner(mn.UL)

        self.play(mn.Write(title2))

        self.wait(2)

        formal = mn.Tex(
            r"Una relación R es un subconjunto de: $D1 \times D2 \times ... \times Dn$",
            font_size=40,
        )

        formal.to_corner(mn.UL).shift(1 * mn.DOWN)

        tupla = mn.Tex(
            "Una tupla es un elemento de R de la forma t = (v1, v2, ..., vn)",
            font_size=40,
        )

        tupla.next_to(formal, mn.DOWN)
        tupla.to_corner(mn.LEFT)

        self.play(mn.Write(formal))

        self.wait(2)

        self.play(mn.Write(tupla))

        self.wait(5)

        self.play(mn.FadeOut(title2), mn.FadeOut(formal), mn.FadeOut(tupla))

        self.wait(2)

        ##TODO: Explicar operadores

        title2 = mn.Text("Operadores", font_size=60)
        title2_1 = mn.Text("Selección", font_size=60)
        self.play(mn.Write(title2))

        self.wait(2)

        self.play(mn.Transform(title2, title2_1))

        self.wait(2)

        self.play(mn.FadeOut(title2))

        ##Selección
        ## Selecciona tuplas que satiface una condición dada.

        seleccion = mn.Tex(
            r"$\text{El operador seleccion se escribe de la forma: } \sigma_p(r)$",
            font_size=50,
        )

        ##Ejemplo de seleccion con la tabla de nombre apellido

        seleccion_nombre_apellido = mn.Tex(
            r"$\sigma_{Nombre = \text{Peter}}(\text{nombre\_apellido})$", font_size=50
        )
        table2_truncated = mn.Table(
            [["Peter", "Parker"]],
            row_labels=[mn.Text("1", color=mn.PURPLE)],
            col_labels=[
                mn.Text("Nombre", color=mn.RED),
                mn.Text("Apellido", color=mn.RED),
            ],
            include_outer_lines=True,
            line_config={"stroke_width": 1, "color": mn.YELLOW},
        )

        table2_truncated.scale(0.6)

        seleccion.to_corner(mn.UL)

        seleccion_nombre_apellido.next_to(seleccion, mn.DOWN)
        seleccion_nombre_apellido.to_corner(mn.LEFT)

        self.play(mn.Write(seleccion))

        self.wait(2)

        self.play(mn.Write(seleccion_nombre_apellido))

        self.wait(2)

        self.play(mn.Write(table2_truncated))

        self.wait(5)

        self.play(
            mn.FadeOut(seleccion),
            mn.FadeOut(seleccion_nombre_apellido),
            mn.FadeOut(table2_truncated),
        )

        self.wait(2)

        ##Proyeccion
        ## Devuelve un conjunto de atributos de una relación con ciertos atributos eliminados. Las tuplas resultantes no tienen duplicados.

        title2_2 = mn.Text("Proyección", font_size=60)

        self.play(mn.Write(title2_2))

        self.wait(2)

        self.play(mn.FadeOut(title2_2))

        proyeccion = mn.Tex(
            r"$\text{El operador proyeccion se representa de la forma: }\prod_{A1, A2, \ldots, An}(r)$",
            font_size=40,
        )

        proyeccion_nombre = mn.Tex(r"$\prod_{Nombre}(nombre\_apellido)$", font_size=40)

        proyeccion_nombre.to_corner(mn.UL).shift(1 * mn.DOWN)

        table2_truncated = mn.Table(
            [["Peter"], ["Clark"]],
            row_labels=[mn.Text("1", color=mn.PURPLE), mn.Text("2", color=mn.PURPLE)],
            col_labels=[mn.Text("Nombre", color=mn.RED)],
            include_outer_lines=True,
            line_config={"stroke_width": 1, "color": mn.YELLOW},
        )

        proyeccion_nombre_con_seleccion = mn.Tex(
            r"$\prod_{Nombre}(\sigma_{Nombre = \text{Peter}}(nombre\_apellido))$",
            font_size=40,
        )

        proyeccion_nombre_con_seleccion.to_corner(mn.UL).shift(1 * mn.DOWN)

        table2_truncated_selected = mn.Table(
            [["Peter"]],
            row_labels=[mn.Text("1", color=mn.PURPLE)],
            col_labels=[mn.Text("Nombre", color=mn.RED)],
            include_outer_lines=True,
            line_config={"stroke_width": 1, "color": mn.YELLOW},
        )

        table2_truncated_selected.scale(0.6)

        proyeccion.to_corner(mn.UL)

        self.play(mn.Write(proyeccion))

        self.wait(2)

        self.play(mn.Write(proyeccion_nombre))

        self.wait(2)

        self.play(mn.Write(table2_truncated))

        self.wait(5)

        self.play(mn.Transform(proyeccion_nombre, proyeccion_nombre_con_seleccion))

        self.wait(2)

        self.play(mn.Transform(table2_truncated, table2_truncated_selected))

        self.wait(4)

        self.play(
            mn.FadeOut(proyeccion),
            mn.FadeOut(proyeccion_nombre),
            mn.FadeOut(proyeccion_nombre_con_seleccion),
            mn.FadeOut(table2_truncated_selected),
            mn.FadeOut(table2_truncated),
        )

        ##Operador Union
        ## Devuelve la unión de dos relaciones. Las tuplas duplicadas son eliminadas.

        title2_3 = mn.Text("Unión", font_size=60)

        self.play(mn.Write(title2_3))

        self.wait(2)

        self.play(mn.FadeOut(title2_3))

        union = mn.Tex(
            r"$\text{El operador unión se representa de la forma: } r \cup s$",
            font_size=40,
        )
        union.to_corner(mn.UL)

        union_nombre = mn.Tex(
            r"$nombre\_apellido \cup nombre\_apellido_{2}$", font_size=40
        )

        union_nombre.to_corner(mn.UL).shift(1 * mn.DOWN)

        table3 = mn.Table(
            [["Peter", "Parker"], ["Tony", "Stark"], ["Bruce", "Wayne"]],
            row_labels=[
                mn.Text("1", color=mn.PURPLE),
                mn.Text("2", color=mn.PURPLE),
                mn.Text("3", color=mn.PURPLE),
            ],
            col_labels=[
                mn.Text("Nombre", color=mn.RED),
                mn.Text("Apellido", color=mn.RED),
            ],
            include_outer_lines=True,
            line_config={"stroke_width": 1, "color": mn.YELLOW},
        )
        table3.scale(0.6)
        table2.scale(0.6)

        self.play(mn.Write(union))

        self.wait(2)

        table2 = mn.Table(
            [["Peter", "Parker"], ["Clark", "Kent"]],
            row_labels=[mn.Text("1", color=mn.PURPLE), mn.Text("2", color=mn.PURPLE)],
            col_labels=[
                mn.Text("Nombre", color=mn.RED),
                mn.Text("Apellido", color=mn.RED),
            ],
            include_outer_lines=True,
            line_config={"stroke_width": 1, "color": mn.YELLOW},
        )

        table2.scale(0.6)

        self.play(mn.Write(table2))

        self.wait(2)

        self.play(mn.Transform(table2, table3))

        self.wait(2)

        self.play(mn.Write(union_nombre))

        self.wait(5)

        ##Nueva tabla union tabla2 y tabla3
        table4 = mn.Table(
            [
                ["Peter", "Parker"],
                ["Clark", "Kent"],
                ["Tony", "Stark"],
                ["Bruce", "Wayne"],
            ],
            row_labels=[
                mn.Text("1", color=mn.PURPLE),
                mn.Text("2", color=mn.PURPLE),
                mn.Text("3", color=mn.PURPLE),
                mn.Text("4", color=mn.PURPLE),
            ],
            col_labels=[
                mn.Text("Nombre", color=mn.RED),
                mn.Text("Apellido", color=mn.RED),
            ],
            include_outer_lines=True,
            line_config={"stroke_width": 1, "color": mn.YELLOW},
        )
        table4.scale(0.6)

        self.play(mn.Transform(table2, table4))

        self.wait(5)

        self.play(mn.FadeOut(union), mn.FadeOut(union_nombre), mn.FadeOut(table2))

        self.wait(2)

        ##Operador Diferencia de Conjuntos
        ## Devuelve las tuplas que están en r pero no en s.

        title2_4 = mn.Text("Diferencia de Conjuntos", font_size=60)

        self.play(mn.Write(title2_4))

        self.wait(2)

        self.play(mn.FadeOut(title2_4))

        diferencia = mn.Tex(
            r"$\text{El operador diferencia de conjuntos se representa de la forma: } r - s$",
            font_size=40,
        )

        diferencia.to_corner(mn.UL)

        diferencia_nombre = mn.Tex(
            r"$nombre\_apellido - nombre\_apellido_{2}$", font_size=40
        )

        diferencia_nombre.to_corner(mn.UL).shift(1 * mn.DOWN)

        table5 = mn.Table(
            [["Clark", "Kent"]],
            row_labels=[mn.Text("1", color=mn.PURPLE)],
            col_labels=[
                mn.Text("Nombre", color=mn.RED),
                mn.Text("Apellido", color=mn.RED),
            ],
            include_outer_lines=True,
            line_config={"stroke_width": 1, "color": mn.YELLOW},
        )
        table5.scale(0.6)

        self.play(mn.Write(diferencia))

        self.wait(2)

        table2 = mn.Table(
            [["Peter", "Parker"], ["Clark", "Kent"]],
            row_labels=[mn.Text("1", color=mn.PURPLE), mn.Text("2", color=mn.PURPLE)],
            col_labels=[
                mn.Text("Nombre", color=mn.RED),
                mn.Text("Apellido", color=mn.RED),
            ],
            include_outer_lines=True,
            line_config={"stroke_width": 1, "color": mn.YELLOW},
        )
        table2.scale(0.6)

        self.play(mn.Write(table2))

        self.wait(2)

        self.play(mn.Transform(table2, table3))

        self.wait(2)

        self.play(mn.Write(diferencia_nombre))

        self.wait(5)

        self.play(mn.Transform(table2, table5))

        self.wait(5)

        self.play(
            mn.FadeOut(diferencia), mn.FadeOut(diferencia_nombre), mn.FadeOut(table2)
        )

        self.wait(2)

        ##Producto Cartesiano
        ## Devuelve todas las combinaciones posibles de tuplas de dos relaciones

        title2_5 = mn.Text("Producto Cartesiano", font_size=60)

        self.play(mn.Write(title2_5))

        self.wait(2)

        self.play(mn.FadeOut(title2_5))

        producto = mn.Tex(
            r"$\text{El operador producto cartesiano se representa de la forma: } r \times s$",
            font_size=40,
        )

        producto.to_corner(mn.UL)

        producto_nombre = mn.Tex(
            r"$nombre\_apellido \times nombre\_apellido$", font_size=40
        )

        producto_nombre.to_corner(mn.UL).shift(1 * mn.DOWN)

        table6 = mn.Table(
            [
                ["Peter", "Parker"],
                ["Peter", "Kent"],
                ["Clark", "Kent"],
                ["Clark", "Parker"],
            ],
            row_labels=[
                mn.Text("1", color=mn.PURPLE),
                mn.Text("2", color=mn.PURPLE),
                mn.Text("3", color=mn.PURPLE),
                mn.Text("4", color=mn.PURPLE),
            ],
            col_labels=[
                mn.Text("Nombre", color=mn.RED),
                mn.Text("Apellido", color=mn.RED),
            ],
            include_outer_lines=True,
            line_config={"stroke_width": 1, "color": mn.YELLOW},
        )
        table6.scale(0.6)

        self.play(mn.Write(producto))

        self.wait(2)

        table2 = mn.Table(
            [["Peter", "Parker"], ["Clark", "Kent"]],
            row_labels=[mn.Text("1", color=mn.PURPLE), mn.Text("2", color=mn.PURPLE)],
            col_labels=[
                mn.Text("Nombre", color=mn.RED),
                mn.Text("Apellido", color=mn.RED),
            ],
            include_outer_lines=True,
            line_config={"stroke_width": 1, "color": mn.YELLOW},
        )
        table2.scale(0.6)

        self.play(mn.Write(table2))

        self.wait(2)

        self.play(mn.Write(producto_nombre))

        self.wait(5)

        self.play(mn.Transform(table2, table6))

        self.wait(5)

        self.play(mn.FadeOut(producto), mn.FadeOut(producto_nombre), mn.FadeOut(table2))

        self.wait(2)

        ##Renombramiento
        ## Cambia el nombre de las relaciones

        title2_6 = mn.Text("Renombramiento", font_size=60)

        self.play(mn.Write(title2_6))

        self.wait(2)

        self.play(mn.FadeOut(title2_6))

        renombramiento = mn.Tex(
            r"$\text{El operador renombramiento se representa de la forma: } \rho_{x}(E)$",
            font_size=40,
        )
        renombramiento.to_corner(mn.UL)
        renombramiento_nombre = mn.Tex(
            r"$\rho_{\text{Nombres superheroes}}(nombre\_apellido)$", font_size=40
        )

        renombramiento_nombre.to_corner(mn.UL).shift(1 * mn.DOWN)

        nombre_tabla = mn.Text("nombre_apellido", font_size=25)

        nombre_tabla.to_corner(mn.UL).shift(2 * mn.DOWN)

        nombre_tabla_new = mn.Text("nombre_superheroes", font_size=25)

        nombre_tabla_new.to_corner(mn.UL).shift(2 * mn.DOWN)

        ##En este momento table2 se llama nombre_apellido
        ##Al aplicar el renombramiento, table2 se llamará nombre_superheroes

        self.play(mn.Write(renombramiento))

        self.wait(2)
        table2 = mn.Table(
            [["Peter", "Parker"], ["Clark", "Kent"]],
            row_labels=[mn.Text("1", color=mn.PURPLE), mn.Text("2", color=mn.PURPLE)],
            col_labels=[
                mn.Text("Nombre", color=mn.RED),
                mn.Text("Apellido", color=mn.RED),
            ],
            include_outer_lines=True,
            line_config={"stroke_width": 1, "color": mn.YELLOW},
        )

        table2.scale(0.6)

        self.play(mn.Write(table2))

        self.wait(2)

        self.play(mn.Write(renombramiento_nombre))

        self.wait(2)

        self.play(mn.Write(nombre_tabla))

        self.wait(2)

        self.play(mn.Transform(nombre_tabla, nombre_tabla_new))

        self.wait(5)

        self.play(
            mn.FadeOut(renombramiento),
            mn.FadeOut(renombramiento_nombre),
            mn.FadeOut(nombre_tabla),
            mn.FadeOut(nombre_tabla_new),
            mn.FadeOut(table2),
        )

        self.wait(2)

        ## Otras operaciones
        ## Las operaciones ya mencionadas sirven para realiar cualquier consulta, pero existen otras operaciones que son útiles para realizar consultas más complejas.

        title2_7 = mn.Text("Otras Operaciones", font_size=60)

        self.play(mn.Write(title2_7))

        self.wait(2)

        self.play(mn.FadeOut(title2_7))

        ##Intersección
        titke2_8 = mn.Text("Intersección", font_size=60)

        self.play(mn.Write(titke2_8))

        self.wait(2)

        self.play(mn.FadeOut(titke2_8))

        interseccion_original = mn.Tex(
            r"$\text{Este operador fue creado para representar de una forma más simple la}$",
            font_size=40,
        )
        interseccion_line2 = mn.Tex(
            r"$\text{operación r - (r - s)}$",
            font_size=40,
        )

        interseccion_original.to_corner(mn.UL)
        interseccion_line2.to_corner(mn.UL).shift(0.5 * mn.DOWN)

        interseccion = mn.Tex(
            r"$\text{El operador intersección se representa de la forma: } r \cap s$",
            font_size=40,
        )

        interseccion.to_corner(mn.UL)

        interseccion_nombre = mn.Tex(
            r"$nombre\_apellido \cap nombre\_apellido_{2}$", font_size=40
        )

        interseccion_nombre.to_corner(mn.UL).shift(1 * mn.DOWN)

        table2 = mn.Table(
            [["Peter", "Parker"], ["Clark", "Kent"]],
            row_labels=[mn.Text("1", color=mn.PURPLE), mn.Text("2", color=mn.PURPLE)],
            col_labels=[
                mn.Text("Nombre", color=mn.RED),
                mn.Text("Apellido", color=mn.RED),
            ],
            include_outer_lines=True,
            line_config={"stroke_width": 1, "color": mn.YELLOW},
        )

        table2.scale(0.6)

        table3 = mn.Table(
            [["Peter", "Parker"], ["Tony", "Stark"], ["Bruce", "Wayne"]],
            row_labels=[
                mn.Text("1", color=mn.PURPLE),
                mn.Text("2", color=mn.PURPLE),
                mn.Text("3", color=mn.PURPLE),
            ],
            col_labels=[
                mn.Text("Nombre", color=mn.RED),
                mn.Text("Apellido", color=mn.RED),
            ],
            include_outer_lines=True,
            line_config={"stroke_width": 1, "color": mn.YELLOW},
        )

        table3.scale(0.6)

        table7 = mn.Table(
            [["Peter", "Parker"]],
            row_labels=[mn.Text("1", color=mn.PURPLE)],
            col_labels=[
                mn.Text("Nombre", color=mn.RED),
                mn.Text("Apellido", color=mn.RED),
            ],
            include_outer_lines=True,
            line_config={"stroke_width": 1, "color": mn.YELLOW},
        )

        table7.scale(0.6)

        self.play(mn.Write(interseccion_original))
        self.play(mn.Write(interseccion_line2))

        self.wait(5)

        self.play(
            mn.Transform(interseccion_original, interseccion),
            mn.Transform(interseccion_line2, interseccion),
        )

        self.wait(5)

        self.play(mn.Write(interseccion_nombre))

        self.wait(2)

        self.play(mn.Write(table2))

        self.wait(2)

        self.play(mn.Transform(table2, table3))

        self.wait(2)

        self.play(mn.Transform(table2, table7))

        self.wait(5)

        self.play(
            mn.FadeOut(interseccion),
            mn.FadeOut(interseccion_nombre),
            mn.FadeOut(table2),
            mn.FadeOut(interseccion_original),
            mn.FadeOut(interseccion_line2),
        )

        self.wait(2)

        ##Reunión Natural
        ## Es igual al producto cartesiano, pero sin repetir tuplas que tengan los mismos valores en los atributos comunes.

        title2_8 = mn.Text("Reunión Natural", font_size=60)

        self.play(mn.Write(title2_8))

        self.wait(2)

        self.play(mn.FadeOut(title2_8))

        reunion = mn.Tex(
            r"$\text{El operador reunión natural se representa de la forma: } r \bowtie_{\text{join condition}} s$",
            font_size=40,
        )

        reunion.to_corner(mn.UL)

        reunion_nombre = mn.Tex(
            r"$nombre\_apellido \bowtie_{\text{nombre='Bruce'}} nombre\_apellido_{2}$",
            font_size=40,
        )

        reunion_nombre.to_corner(mn.UL).shift(1 * mn.DOWN)

        table8 = mn.Table(
            [["Bruce", "Banner"], ["Clark", "Kent"]],
            row_labels=[mn.Text("1", color=mn.PURPLE), mn.Text("2", color=mn.PURPLE)],
            col_labels=[
                mn.Text("Nombre", color=mn.RED),
                mn.Text("Apellido", color=mn.RED),
            ],
            include_outer_lines=True,
            line_config={"stroke_width": 1, "color": mn.YELLOW},
        )

        table8.scale(0.6)

        table9 = mn.Table(
            [["Peter", "Parker"], ["Bruce", "Wayne"]],
            row_labels=[mn.Text("1", color=mn.PURPLE), mn.Text("2", color=mn.PURPLE)],
            col_labels=[
                mn.Text("Nombre", color=mn.RED),
                mn.Text("Apellido", color=mn.RED),
            ],
            include_outer_lines=True,
            line_config={"stroke_width": 1, "color": mn.YELLOW},
        )

        table9.scale(0.6)

        ##En este caso, la reunión natural de table8 y table9 es table10 que contiene a Bruce Wayne y Bruce Banner

        table10 = mn.Table(
            [["Bruce", "Banner"], ["Bruce", "Wayne"]],
            row_labels=[mn.Text("1", color=mn.PURPLE), mn.Text("2", color=mn.PURPLE)],
            col_labels=[
                mn.Text("Nombre", color=mn.RED),
                mn.Text("Apellido", color=mn.RED),
            ],
            include_outer_lines=True,
            line_config={"stroke_width": 1, "color": mn.YELLOW},
        )

        table10.scale(0.6)

        self.play(mn.Write(reunion))

        self.wait(2)

        self.play(mn.Write(table8))

        self.wait(2)

        self.play(mn.Transform(table8, table9))

        self.wait(2)

        self.play(mn.Write(reunion_nombre))

        self.wait(2)

        self.play(mn.Transform(table8, table10))

        self.wait(5)

        self.play(mn.FadeOut(reunion), mn.FadeOut(reunion_nombre), mn.FadeOut(table8))

        ## Operador asignación, utiliza una flecha apuntando hacia la izquierda y se utiliza para asignar un valor a una variable.

        title2_10 = mn.Text("Asignación", font_size=60)

        self.play(mn.Write(title2_10))

        self.wait(2)

        self.play(mn.FadeOut(title2_10))

        asignacion = mn.Tex(
            r"$\text{El operador asignación se representa de la forma: } x \leftarrow E$",
            font_size=40,
        )

        asignacion.to_corner(mn.UL)

        asignacion_explicacion = mn.Text(
            "Se utiliza para asignar un valor a una variable", font_size=30
        )

        asignacion_explicacion.to_corner(mn.UL).shift(1 * mn.DOWN)

        self.play(mn.Write(asignacion))

        self.wait(2)

        self.play(mn.Write(asignacion_explicacion))

        self.wait(5)

        self.play(mn.FadeOut(asignacion), mn.FadeOut(asignacion_explicacion))

        self.wait(5)

        ##Funciones de Agregación

        title2_11 = mn.Text("Funciones de Agregación", font_size=60)

        self.play(mn.Write(title2_11))

        self.wait(2)

        self.play(mn.FadeOut(title2_11))

        ##Funciones de agregación

        agregacion = mn.Text(
            "Las funciones de agregación son funciones que operan sobre ",
            font_size=30,
        )
        agregacion_line2 = mn.Text(
            "un conjunto de valores y devuelven un único valor.",
            font_size=30,
        )

        agregacion.to_corner(mn.UL)
        agregacion_line2.to_corner(mn.UL).shift(0.5 * mn.DOWN)

        funcion_suma = mn.Tex(r"$\sum_{i=1}^{n} x_i$", font_size=40)

        funcion_suma.to_corner(mn.UL).shift(1 * mn.DOWN)

        funcion_promedio = mn.Tex(r"$\frac{1}{n} \sum_{i=1}^{n} x_i$", font_size=40)

        funcion_promedio.to_corner(mn.UL).shift(2 * mn.DOWN)

        funcion_max = mn.Tex(r"$\max_{i=1}^{n} x_i$", font_size=40)

        funcion_max.to_corner(mn.UL).shift(3 * mn.DOWN)

        funcion_min = mn.Tex(r"$\min_{i=1}^{n} x_i$", font_size=40)

        funcion_min.to_corner(mn.UL).shift(4 * mn.DOWN)

        funcion_count = mn.Tex(r"$\text{count}(x_i)$", font_size=40)

        funcion_count.to_corner(mn.UL).shift(5 * mn.DOWN)

        self.play(mn.Write(agregacion))
        self.play(mn.Write(agregacion_line2))

        self.wait(2)

        self.play(
            mn.Write(funcion_suma),
            mn.Write(funcion_promedio),
            mn.Write(funcion_max),
            mn.Write(funcion_min),
            mn.Write(funcion_count),
        )

        self.wait(5)

        self.play(
            mn.FadeOut(agregacion),
            mn.FadeOut(funcion_suma),
            mn.FadeOut(funcion_promedio),
            mn.FadeOut(funcion_max),
            mn.FadeOut(funcion_min),
            mn.FadeOut(funcion_count),
            mn.FadeOut(agregacion_line2),
        )

        self.wait(2)
