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
        top_left_text = mn.Text("An: Atributo 'n'\n \n Tn: Tupla 'n' \n \n Vn: Valor 'n'", font_size=30)
        top_left_text.to_corner(mn.UL).shift(0.5 * mn.LEFT)
        self.play(mn.Write(top_left_text))
        self.wait(2)
        ##Table

        table = mn.Table(
            [["V1", "V2"],
            ["V1", "V2"]],
            row_labels=[mn.Text("T1",color=mn.PURPLE), mn.Text("T2", color=mn.PURPLE)],
            col_labels=[mn.Text("A1", color=mn.RED), mn.Text("A2", color=mn.RED)],
            top_left_entry=mn.Star(color=mn.YELLOW).scale(0.3),
            include_outer_lines=True,
            line_config={"stroke_width": 1, "color": mn.YELLOW}
           
        )
        
        
        self.play(mn.Write(table))
        self.wait(2)

        # Highlight the col labels
        highlight_col_label_1 = table.get_highlighted_cell((1, 2), color=mn.GREEN)
        highlight_col_label_2 = table.get_highlighted_cell((1, 3), color=mn.GREEN)
        self.add(highlight_col_label_1,highlight_col_label_2)  # Add the highlighted cell to the scene
        self.play(mn.FadeIn(highlight_col_label_1),mn.FadeIn(highlight_col_label_2))  # Fade in the highlighted cell
        

        self.wait(2)
        self.play(mn.FadeOut(highlight_col_label_1), mn.FadeOut(highlight_col_label_2))

        self.wait(2)

        #highlight the row labels
        highlight_row_label_1 = table.get_highlighted_cell((2, 1), color=mn.GREEN)
        highlight_row_label_2 = table.get_highlighted_cell((3, 1), color=mn.GREEN)
        self.add(highlight_row_label_1,highlight_row_label_2)
        self.play(mn.FadeIn(highlight_row_label_1),mn.FadeIn(highlight_row_label_2))

        self.wait(2)
        self.play(mn.FadeOut(highlight_row_label_1), mn.FadeOut(highlight_row_label_2))

        self.wait(2)

        #highlight each value in succession
        highlight_value_1 = table.get_highlighted_cell((2, 2), color=mn.GREEN)
        highlight_value_2 = table.get_highlighted_cell((2, 3), color=mn.GREEN)
        highlight_value_3 = table.get_highlighted_cell((3, 2), color=mn.GREEN)
        highlight_value_4 = table.get_highlighted_cell((3, 3), color=mn.GREEN)

        self.play(mn.FadeIn(highlight_value_1))
        self.play(mn.FadeIn(highlight_value_2)) 
        self.play(mn.FadeIn(highlight_value_3))
        self.play(mn.FadeIn(highlight_value_4))

        self.wait(2)

        self.play(mn.FadeOut(highlight_value_1), mn.FadeOut(highlight_value_2), mn.FadeOut(highlight_value_3), mn.FadeOut(highlight_value_4))

        
        self.wait(5)

        ## Table with actual example

        table2 = mn.Table(
            [["Peter", "Parker"],
            ["Clark", "Kent"]],
            row_labels=[mn.Text("1",color=mn.PURPLE), mn.Text("2", color=mn.PURPLE)],
            col_labels=[mn.Text("Nombre", color=mn.RED), mn.Text("Apellido", color=mn.RED)],
            include_outer_lines=True,
            line_config={"stroke_width": 1, "color": mn.YELLOW}
        )


        self.play(mn.FadeOut(top_left_text),mn.Transform(table, table2))

        self.wait(5)
        ##nuevamente resaltamos columnas
        highlight_col_label_1 = table2.get_highlighted_cell((1, 2), color=mn.GREEN)
        highlight_col_label_2 = table2.get_highlighted_cell((1, 3), color=mn.GREEN)
        self.add(highlight_col_label_1,highlight_col_label_2)
        self.play(mn.FadeIn(highlight_col_label_1),mn.FadeIn(highlight_col_label_2))

        self.wait(2)

        self.play(mn.FadeOut(highlight_col_label_1), mn.FadeOut(highlight_col_label_2))

        self.wait(2)
        ##nuevamente resaltamos filas
        highlight_row_label_1 = table2.get_highlighted_cell((2, 1), color=mn.GREEN)
        highlight_row_label_2 = table2.get_highlighted_cell((3, 1), color=mn.GREEN)
        self.add(highlight_row_label_1,highlight_row_label_2)
        self.play(mn.FadeIn(highlight_row_label_1),mn.FadeIn(highlight_row_label_2))

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

        self.play(mn.FadeOut(highlight_value_1), mn.FadeOut(highlight_value_2), mn.FadeOut(highlight_value_3), mn.FadeOut(highlight_value_4))

        self.wait(5)


        ##resaltamos dominio 

        TextoDominio = mn.Text("Dominio: Conjunto de valores que puede tomar un atributo", font_size=30)
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

        Subconjunto = mn.Tex('Tabla = D1 x D2')
        Subconjunto.to_corner(mn.UL)

        self.play(mn.Write(Subconjunto))

        self.wait(2)

        
        self.play(mn.FadeOut(table,table2))

        self.wait(2)

    ##Definicion Formal


    ##TODO: Explicar operadores

        title2 = mn.Text("Operadores", font_size=60)
        self.play(mn.Write(title2))









