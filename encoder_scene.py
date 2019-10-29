from manimlib.imports import *

class Node(Circle): # Node object shape circle has list of outputs
    def __init__(self):
        super(Node,self).__init__(fill_color="#003687",fill_opacity=1,stroke_width=2.5)
        self.set_stroke("#F4CC29")
        self.outputs = []

    def addOutput(self,item):
        self.outputs.append(item)

    def getLines(self):
        return VGroup(*[Line(self.get_center(),item.get_center(),stroke_width=0.6,stroke_color="#A1BAC9") for item in self.outputs])


class ArrayTest(Scene):
    def construct(self):
        text_b = TextMobject("Aplikujeme ", "filtre").to_edge(UP);
        text = TextMobject("Čo robia ", "filtre", "?").scale(2);
        self.play(Write(text_b));
        self.wait()
        self.play(Write(text[0]),Write(text[2]),Transform(text_b[1],text[1]),Uncreate(text_b[0]));
        self.wait()



class LatentFaces(Scene):
    def construct(self):
        input_face = Square().to_edge(LEFT).scale(0.8)
        output_face = Square().to_edge(RIGHT).scale(0.8)
        latent_face = Square().scale(0.8)
        encoder = Polygon(UL,UR+DOWN/3,DR+UP/3,DL).scale(0.8)
        decoder = Polygon(UL+DOWN/3,UR,DR,DL+UP/3).scale(0.8)

        encoder.move_to(2.5*LEFT)
        decoder.move_to(2.5*RIGHT)

        self.play(Write(encoder),Write(input_face),Write(decoder),Write(latent_face),Write(output_face))

        input_arrow = Arrow(input_face.get_right(),encoder.get_left(),buff=0)
        encoder_latent_arrow = Arrow(encoder.get_right(),latent_face.get_left(),buff=0)
        latent_decoder_arrow = Arrow(latent_face.get_right(),decoder.get_left(),buff=0)
        output_arrow = Arrow(decoder.get_right(),output_face.get_left(),buff=0)
        arrows = VGroup(input_arrow,encoder_latent_arrow,latent_decoder_arrow,output_arrow)
        self.play(Write(arrows))
        self.wait()
        network = VGroup(input_face,output_face,latent_face,encoder,decoder,arrows)
        network_copy = network.copy()
        self.play(network.move_to,2*UP,network_copy.move_to,2*DOWN)
        self.wait(2)
        self.play(Uncreate(latent_decoder_arrow),Uncreate(network_copy[5][2]))
        new_arrow_a = Line(latent_face.get_bottom(),network_copy[4].get_left(),buff=0)
        new_arrow_b = Line(network_copy[2].get_top(),decoder.get_left(),buff=0)
        new_arrows = VGroup(new_arrow_a,new_arrow_b)
        self.play(Write(new_arrows))
        self.wait(2)
        whole_scene = VGroup(network,network_copy,new_arrows)
        self.wait(2)
        self.play(Uncreate(whole_scene))


class Dragana(Scene):
    def construct(self):
        text = TextMobject("""Webové technologie sú veľmi\\\\ zaujímavý predmet""").scale(1.8);
        text2 = TextMobject("Mám rád Webové technologie").scale(2)

        self.add(text)
        self.wait()
        self.play(Transform(text,text2))
        self.wait(2)
        self.play(Transform(text2,text))

class Pixel(Scene):
    def construct(self):

        pixel = Circle(stroke_width=5,stroke_color=YELLOW,fill_opacity=1,fill_color=BLACK)
        self.play(Write(pixel))
        pixel_text = TextMobject("Pixel").move_to(pixel.get_top()+UP)
        self.play(Write(pixel_text))
        r_input = Circle(fill_color="#FF0000", fill_opacity=1, stroke_width=0)
        g_input = Circle(fill_color="#3cff00", fill_opacity=1, stroke_width=0)
        b_input = Circle(fill_color="#0004ff", fill_opacity=1, stroke_width=0)
        color_inputs = VGroup(r_input,g_input,b_input).arrange(RIGHT)
        color_hint_box = SurroundingRectangle(color_inputs,buff=MED_LARGE_BUFF)
        color_hint_text = TextMobject("Každý pixel má tri hodnoty").move_to(color_hint_box.get_top()+UP/2)
        color_hint = VGroup(color_hint_box,color_hint_text)

        self.play(ReplacementTransform(pixel.copy(),color_inputs))
        self.play(Write(color_hint_box))
        self.play(ReplacementTransform(pixel_text,color_hint_text))
        self.wait()
        self.play(Uncreate(color_hint),Uncreate(color_hint_text))
        self.play(ReplacementTransform(color_inputs,pixel))

        r_l = Line(2.5*LEFT,2.5*RIGHT)
        r_t = TextMobject("R").move_to(r_l.get_start()+LEFT/2)
        g_l = Line(2.5*LEFT,2.5*RIGHT)
        g_t = TextMobject("G").move_to(g_l.get_start()+LEFT/2)
        b_l = Line(2.5*LEFT,2.5*RIGHT)
        b_t = TextMobject("B").move_to(b_l.get_start()+LEFT/2)
        r_dot = Dot().move_to(r_l.get_start())
        g_dot = Dot().move_to(g_l.get_start())
        b_dot = Dot().move_to(b_l.get_start())
        r_n = Integer(0).move_to(r_l.get_right()+MED_SMALL_BUFF+DOWN/4)

        g_n = Integer(0).move_to(g_l.get_right()+MED_SMALL_BUFF+DOWN/4)
        b_n = Integer(0).move_to(b_l.get_right()+MED_SMALL_BUFF+DOWN/4)
        r = VGroup(r_dot,r_l,r_n,r_t)
        g = VGroup(g_dot,g_l,g_n,g_t)
        b = VGroup(b_dot,b_l,b_n,b_t)


        colors = VGroup(r,g,b).arrange(DOWN,buff=MED_LARGE_BUFF).to_edge(DOWN)

        pixel_group = VGroup(pixel,colors)

        pixel_text = TextMobject("Každý vstup je pixel").to_edge(RIGHT)
        pixel_text_next = TextMobject("Každý pixel má tri hodnoty")

        r_n.add_updater(lambda d: d.set_value((r_dot.get_center()[0]-r_l.get_start()[0])*51))
        g_n.add_updater(lambda d: d.set_value((g_dot.get_center()[0]-g_l.get_start()[0])*51))
        b_n.add_updater(lambda d: d.set_value((b_dot.get_center()[0]-b_l.get_start()[0])*51))

        pixel.add_updater(lambda d: d.set_fill('#%02x%02x%02x' % (r_n.get_value(), g_n.get_value(), b_n.get_value())))
        start = True
        self.play(Write(colors))

        for i in range(2):
            if start:
                self.play(r_dot.move_to,r_l.get_end())
                self.play(g_dot.move_to,g_l.get_end())
                self.play(b_dot.move_to,b_l.get_end())
                start = False
            else:
                self.play(r_dot.move_to,r_l.get_center())
                self.play(g_dot.move_to,g_l.get_center())
                self.play(b_dot.move_to,b_l.get_center())
                start = True

        self.wait()


class ImageArrowTest(Scene):
    def construct(self):
        i = ImageMobject("filter_one")
        k = ImageMobject("filter_two")
        l = ImageMobject("filter_three")
        g = Group(i,k,l).arrange(RIGHT,buff=MED_LARGE_BUFF)
        arrow = Arrow(i.get_right(),k.get_left(),buff=0)
        self.play(FadeIn(g),Write(arrow))



class Credits(Scene):
    title_size = 0.85
    desc_size = 0.75
    CONFIG={
        "camera_config":{"background_color":"#003687"},
        "video" : TextMobject("""\\textsc{Autor}""", color=YELLOW,background_stroke_width=0).scale(title_size),
        "video_2" : TextMobject("Žeľko Urban ",background_stroke_width=0).scale(desc_size),
        "video_3" : TextMobject("študent STU FEI", background_stroke_width=0).scale(desc_size),

        "animation" : TextMobject("""\\textsc{Animované pomocou}""", color=YELLOW,background_stroke_width=0).scale(title_size),
        "animation_1" : TextMobject("Knižnica manim autora 3blue1brown",background_stroke_width=0).scale(desc_size),

        "libraries" : TextMobject("""\\textsc{Knižnice}""", color=YELLOW,background_stroke_width=0).scale(title_size),
        "libraries_1" : TextMobject("DeepFaceLab",background_stroke_width=0).scale(desc_size),
        "libraries_2" : TextMobject("ffmpeg",background_stroke_width=0).scale(desc_size),
        "libraries_3" : TextMobject("S3FD",background_stroke_width=0).scale(desc_size),

        "thanks" : TextMobject("""\\textsc{Poďakovanie}""", color=YELLOW,background_stroke_width=0).scale(title_size),
        "thanks_1" : TextMobject("Michal Klimek",background_stroke_width=0).scale(desc_size),
        "thanks_2" : TextMobject("IBM Slovensko",background_stroke_width=0).scale(desc_size),

        "date" : TextMobject("""Október 2019""",color = YELLOW,background_stroke_width=0).scale(desc_size)

    }
    def construct(self):
        text_size = 0.6
        video = VGroup(self.video,self.video_2,self.video_3).arrange(DOWN,buff=SMALL_BUFF)
        animation = VGroup(self.animation,self.animation_1).arrange(DOWN,buff=SMALL_BUFF)
        libraries = VGroup(self.libraries,self.libraries_1,self.libraries_2,self.libraries_3).arrange(DOWN,buff=SMALL_BUFF)
        thanks = VGroup(self.thanks,self.thanks_1,self.thanks_2).arrange(DOWN,buff=SMALL_BUFF)
        credits = VGroup(video,libraries,animation,thanks,self.date).arrange(DOWN,buff=MED_LARGE_BUFF)

        self.play(Write(credits))
        self.wait(12)
        self.play(Uncreate(credits))
        self.wait()


class Facts(MovingCameraScene):
    CONFIG = {
    "camera_config" : {"background_color":"#003687"}
    }
    def construct(self):
        icon_size = 0.5
        title = Title("Ako na deepfake video", tex_to_color_map ={ "deepfake" : YELLOW}, background_stroke_width=0).move_to(ORIGIN)
        ##pc = SVGMobject("computer").scale(icon_size)
        cloud = SVGMobject("cloud").scale(icon_size)
        time = SVGMobject("time").scale(icon_size)
        video = SVGMobject("video").scale(icon_size)
        ##face =SVGMobject("face").scale(icon_size)
        gpu = SVGMobject("gpu").scale(icon_size)
        icons = VGroup(cloud,time,video,gpu).arrange(RIGHT,buff=MED_LARGE_BUFF)



        self.play(Write(title));
        self.camera_frame.save_state()




        p = RegularPolygon(4).scale(3)
        self.wait(2)
        self.play(Uncreate(title))
        #BulletedList("Počitáč","počitáč musí byť dobrého výkonnu",background_stroke_width=0).scale(0.25),
        text = [
                BulletedList("""\\textbf{Cloud}""","IBM Watson Studio","Google Colab",background_stroke_width=0).scale(0.35),
                BulletedList("""\\textbf{Trénovanie}""","15-20 hodín tréningu","Dlhšie trénovanie zlepšuje výsledky",background_stroke_width=0).scale(0.35),
                BulletedList("""\\textbf{Video}""","Kvalitné vstupné video","Okolo 1000 obrázkov novej tváre",background_stroke_width=0).scale(0.35),
                BulletedList("""\\textbf{Grafická karta}""","najlepšie Nvidia CUDA","ideálne viac ako 4GB",background_stroke_width=0).scale(0.35)]
        ##self.play(Write(p))
        ##[(self.play(Transform(p,RegularPolygon(i).scale(3)))) for i in range(3,6)]

        for i in range(len(icons)):
            icons[i].move_to(ORIGIN)
            self.play(Write(icons[i]),icons[i].move_to,p.get_vertices()[i])


        # Save the state of camera

        i = 0
        text_copies = []
        for item in icons:
        # Animation of the camera
            text_desc = text[i]
            text_desc.next_to(item,RIGHT)


            ##text_copies.append(text_desc.copy())
            self.play(

            # Set the size with the width of a object
                self.camera_frame.set_width,item.get_width()*4.2,

            # Move the camera to the object
                self.camera_frame.move_to,item.get_center()+RIGHT+0.7*RIGHT,

                Write(text_desc)
                )
            self.wait(2.3)
            i+=1
            #self.play(Uncreate(text_desc))

        # Restore the state saved
            self.play(Restore(self.camera_frame))
            self.wait(2)



        '''
        self.play(ApplyMethod(pc.move_to,ORIGIN))
        self.play(Write(text_desc));
        box_content = VGroup(pc,text_desc);
        box = SurroundingRectangle(box_content,color=YELLOW,buff=MED_LARGE_BUFF)
        self.play(Write(box))
        self.wait()
        self.play(Uncreate(box))
        self.play(pc.next_to,cloud,UP)
        self.wait()

        self.play(ApplyMethod(cloud.move_to,ORIGIN))
        text_desc_new = TextMobject("Môžeme použiť cloud.").move_to(text_desc)
        self.play(ReplacementTransform(text_desc,text_desc_new));
        box_content = VGroup(cloud,text_desc_new);
        box = SurroundingRectangle(box_content,color=YELLOW,buff=MED_LARGE_BUFF)
        self.play(Write(box))
        self.wait()
        self.play(Uncreate(box))
        self.play(cloud.next_to,time,UP)
        self.wait()

        self.play(ApplyMethod(time.move_to,ORIGIN))
        text_desc = TextMobject("Môžeme použiť time.").move_to(text_desc_new)
        self.play(ReplacementTransform(text_desc_new,text_desc));
        box_content = VGroup(time,text_desc);
        box = SurroundingRectangle(box_content,color=YELLOW,buff=MED_LARGE_BUFF)
        self.play(Write(box))
        self.wait()
        self.play(Uncreate(box))
        self.play(time.next_to,video,UP)
        self.wait()

        self.play(ApplyMethod(video.move_to,ORIGIN))
        text_desc_new = TextMobject("Môžeme použiť video.").move_to(text_desc)
        self.play(ReplacementTransform(text_desc,text_desc_new));
        box_content = VGroup(video,text_desc_new);
        box = SurroundingRectangle(box_content,color=YELLOW,buff=MED_LARGE_BUFF)
        self.play(Write(box))
        self.wait()
        self.play(Uncreate(box))
        self.play(video.next_to,gpu,UP)
        self.wait()

        self.play(ApplyMethod(gpu.move_to,ORIGIN))
        text_desc = TextMobject("Môžeme použiť gpu.").move_to(text_desc_new)
        self.play(ReplacementTransform(text_desc_new,text_desc));
        box_content = VGroup(gpu,text_desc);
        box = SurroundingRectangle(box_content,color=YELLOW,buff=MED_LARGE_BUFF)
        self.play(Write(box))
        self.wait()
        self.play(Uncreate(box))
        self.play(gpu.next_to,video,DOWN)
        self.wait()
        '''

class FinalScene(Scene):
    CONFIG={
        "camera_config":{"background_color":"#003687"},
        }
    def construct(self):
        #####################     PART I: INTRODUCTION   ########################

        title = TextMobject("Ako vzniká DeepFake?", tex_to_color_map ={ "DeepFake" : YELLOW}, background_stroke_width=0)
        title.scale(2)

        video_shape  = Square()
        video_image = ImageMobject("input_frame")
        video_image.add_updater(lambda d: d.move_to(video_shape))
        video_label = TextMobject("Vstupné video", background_stroke_width=0)
        video = VGroup(video_shape,video_label)
        video.arrange(DOWN)

        self.play(Write(title))
        self.wait()
        self.play(Transform(title,video))
        self.play(FadeIn(video_image))
        self.remove(title)

        self.play(video.shift,2*UP)

        video_frames = video_shape.copy()
        frames_group = VGroup(*[video_frames.copy().scale(0.3) for i in range(20)])
        frames_images_group = Group(*[ImageMobject("{:04d}".format(i+811)).scale(0.3) for i in range(len(frames_group))])

        frames_group.arrange(
                RIGHT,
                aligned_edge = LEFT,
                buff=0.4)

        frames_group.to_edge(DOWN)
        [frames_images_group[i].move_to(frames_group[i]) for i in range(len(frames_group))]

        self.play(Transform(video_frames,frames_group))
        self.play(FadeIn(frames_images_group))

        frames_brace = Brace(frames_group, UP)
        frames_label = TextMobject("Video rozdelíme na individuálne obrázky", background_stroke_width=0).next_to(frames_brace,UP)
        self.play(GrowFromCenter(frames_brace),Write(frames_label))
        self.play(FadeOutAndShift(video,UP),FadeOut(video_image))
        self.play(Uncreate(frames_label))
        frame_large_analyze = Square()

        frame_large_analyze.to_edge(UP,buff=2)
        frame_large_analyze.scale(1.45)
        frame_analyze_label = TextMobject("Každý obrázok analyzujeme a vyhľadáme tvár", background_stroke_width=0)
        frame_analyze_label.next_to(frame_large_analyze,DOWN,buff=0.3)
        frame_analyze_group = VGroup(frame_large_analyze,frame_analyze_label)

        self.play(Transform(frames_group[0],frame_large_analyze),
                  Write(frame_analyze_label))
        input_frame = ImageMobject("input_frame").move_to(frame_large_analyze).scale(1.5)
        self.play(FadeIn(input_frame))
        detect_face = Rectangle(height=0.6,width=0.5,color=GREEN_SCREEN,stroke_width=10)
        detect_face.move_to(frame_large_analyze.get_center()+(2*UP)/3)
        detect_face.rotate(-PI/50)
        self.play(Write(detect_face))


        self.play(Transform(detect_face,frame_large_analyze),frame_large_analyze.set_color,GREEN_SCREEN)
        self.play(FadeOut(input_frame))
        input_frame_crop = ImageMobject("input_cropped").move_to(detect_face).scale(1.5)
        self.play(FadeIn(input_frame_crop))
        frame_analyze_label_face = TextMobject("Tvár orežeme a zarovnáme",color=YELLOW, background_stroke_width=0).next_to(frame_large_analyze,DOWN)
        self.play(Transform(frame_analyze_label,frame_analyze_label_face))

        faces_group = VGroup(*[VGroup(*[Square(color=YELLOW).scale(0.5) for i in range(10)]).arrange(RIGHT)for i in range(5)]).arrange(DOWN)
        faces_group_images = Group(*[ImageMobject("{:05d}_0".format(i+794)).scale(0.5) for i in range(50)])
        self.play(Uncreate(frames_label))
        self.play(Uncreate(frames_brace))
        self.play(FadeOut(input_frame_crop))
        self.play(FadeOut(frames_images_group))
        faces_group.to_edge(UP)
        self.remove(detect_face,frame_large_analyze,video_frames)
        self.remove(frame_analyze_label)
        self.play(ReplacementTransform(frames_group,faces_group),frame_analyze_label_face.next_to,faces_group,DOWN)
        [[faces_group_images[10*i + j].move_to(faces_group[i][j]) for j in range(10)] for i in range(5)]
        self.play(FadeIn(faces_group_images))
        self.remove(frames_group)


        text_many_frames = TextMobject("Urobíme pre každý frame",color=YELLOW, background_stroke_width=0)
        text_many_frames.to_edge(DOWN)

        self.wait()
        new_text = TextMobject("Vstupy", background_stroke_width=0).move_to(frame_analyze_label_face)
        self.play(ReplacementTransform(frame_analyze_label_face,new_text))
        self.remove(frame_analyze_label_face)
        self.wait()
        self.play(FadeOut(faces_group_images))


        ######################     PART II: NEURAL NET    #######################
        inputN = 12
        middleN = 6
        outputN = 12
        text_size = 0.6
        node_scale = 0.2
        node_padding = 0.07
        #Node Group Generation

        inputs = VGroup(*[Node().scale(node_scale) for i in range(inputN)])
        middles_a = VGroup(*[Node().scale(node_scale) for i in range(middleN)])
        middles = VGroup(*[Node().scale(node_scale) for i in range(middleN//2)])

        middles_b = VGroup(*[Node().scale(node_scale) for i in range(middleN)])
        outputs = VGroup(*[Node().scale(node_scale) for i in range(outputN)])

        #Node Arrangement DOWN and placement (LEFT, MIDDLE, RIGHT)
        inputs.arrange(DOWN,buff=node_padding) # <- arrangement Down by group
        inputs.to_edge(LEFT,buff=3.5) # <- placement LEFT inputs
        middles_a.arrange(DOWN,buff=node_padding)
        middles_b.arrange(DOWN,buff=node_padding)
        middles.arrange(DOWN,buff=node_padding)

        middles_a.move_to(2*LEFT)
        middles_b.move_to(2*RIGHT)

        outputs.arrange(DOWN,buff=node_padding)
        outputs.to_edge(RIGHT,buff=3.5)
        nodes = VGroup(inputs,middles_a,middles,middles_b,outputs)

        #Creating connections between nodes
        for input in inputs: # <- connecting inputs to middles
            for middle in middles_a:
                input.addOutput(middle)

        [[mid_a.addOutput(mid) for mid in middles] for mid_a in middles_a]
        [[mid.addOutput(mid_b) for mid_b in middles_b] for mid in middles]
        [[mid_b.addOutput(out) for out in outputs] for mid_b in middles_b] # <- middles to outputs
                                                                     # same with list comprehensiom
        self.wait()

        # Getting connections to VGroup
        linesIn = VGroup(*[input.getLines() for input in inputs])
        linesMid_a = VGroup(*[middle.getLines() for middle in middles_a])
        linesMid_b = VGroup(*[middle.getLines() for middle in middles])
        linesOut = VGroup(*[middle.getLines() for middle in middles_b])
        connects = VGroup(linesIn,linesMid_a,linesMid_b,linesOut)


        input_face_box = Square().to_edge(LEFT)
        input_face_image = ImageMobject("input_michal").move_to(input_face_box.get_center())
        input_face_label = TextMobject("Vstupná tvár", background_stroke_width=0).next_to(input_face_box,DOWN).scale(text_size)
        input_face = VGroup(input_face_box,input_face_label)

        self.play(ReplacementTransform(faces_group,input_face_box),ReplacementTransform(new_text,input_face_label))
        self.play(FadeIn(input_face_image))
        self.remove(new_text)
        self.remove(faces_group)
        self.play(Write(connects,run_time=3),Write(nodes,run_time=3))



        inputs_box = SurroundingRectangle(inputs,buff=0.3)
        inputs_label = TextMobject("Vstupy", background_stroke_width=0).next_to(inputs_box,UP)
        inputs_hint = VGroup(inputs_box,inputs_label)

        outputs_box = SurroundingRectangle(outputs,buff=0.3)
        outputs_label = TextMobject("Výstupy", background_stroke_width=0).next_to(outputs_box,UP)
        outputs_hint = VGroup(outputs_box,outputs_label)



        self.play(Write(inputs_hint),Write(outputs_hint))
        self.wait()

        self.play(Uncreate(inputs_hint),Uncreate(outputs_hint))

        encoder = VGroup(inputs,middles_a)
        decoder = VGroup(middles_b,outputs)

        encoder_box = SurroundingRectangle(encoder,color=WHITE,buff=0.4)
        encoder_label = TextMobject("Enkodér", background_stroke_width=0).next_to(encoder_box,UP)
        encoder_hint = VGroup(encoder_box,encoder_label)

        decoder_box = SurroundingRectangle(decoder,color=RED,buff=0.4)
        decoder_label = TextMobject("Dekodér", background_stroke_width=0).next_to(decoder_box,UP)
        decoder_hint = VGroup(decoder_box,decoder_label)

        self.wait(2)
        self.play(Write(encoder_hint),Write(decoder_hint))
        self.wait(2)
        self.play(Uncreate(encoder_hint),Uncreate(decoder_hint))
        self.wait()







        self.play(connects.move_to,DOWN,nodes.move_to,DOWN)

        output_face_box = Square().to_edge(RIGHT)
        output_face_image = ImageMobject("output_michal").move_to(output_face_box.get_center())
        output_face_label = TextMobject("Rekonštruovaná tvár", background_stroke_width=0).next_to(output_face_box,DOWN).scale(text_size)
        output_face = VGroup(output_face_box,output_face_label)



        self.wait()

        inputs_save = inputs.copy()
        input_face_copy = input_face_box.copy()
        output_face_copy = output_face_box.copy()
        inputs_copy = inputs.copy()
        middles_a_copy = middles_a.copy()
        middles_copy = middles.copy()
        middles_b_copy = middles_b.copy()
        outputs_copy = outputs.copy()

        surround_buff = 0.2
        helping_surround = SurroundingRectangle(VGroup(input_face_box,inputs), buff=surround_buff, color=WHITE)
        helping_text = TextMobject("Vstupnú tvár rozdelíme na pixely", background_stroke_width=0).to_edge(UP).scale(text_size)
        helping_text_surround = SurroundingRectangle(helping_text,buff = surround_buff, color=WHITE)
        helping_text_surround.add_updater(lambda l: l.set_width(helping_text.get_width()+surround_buff*2))

        helping = VGroup(helping_surround,helping_text)
        helping_arrow = Arrow(helping_text_surround,helping_surround.get_top()+helping_surround.get_left(),stroke_width=3)
        #helping_arrow_2 = Arrow(helping_text,helping_surround)
        helping_arrow.add_updater(lambda l: l.put_start_and_end_on(helping_text_surround.get_bottom(),helping_surround.get_top()))

        self.play(Write(helping))
        self.play(Write(helping_text_surround))
        self.play(Write(helping_arrow))
        self.play(Transform(input_face_copy,inputs))


        helping_text_next = TextMobject("Pixely posielame na vstup do neurónovej siete", background_stroke_width=0).move_to(helping_text).scale(text_size)
        self.play(Transform(helping_text,helping_text_next))

        helping_surround_next = SurroundingRectangle(inputs, buff=surround_buff, color=WHITE)
        self.play(Transform(helping_surround,helping_surround_next))



        self.play(ShowPassingFlashAround(inputs[0]))



        pixel = Circle(stroke_width=5,stroke_color=YELLOW,fill_opacity=1,fill_color="#2A4E83")

        self.play(ReplacementTransform(input_face_copy[0].copy(),pixel))
        self.play(FadeOut(inputs_copy),
                  FadeOut(inputs),
                  FadeOut(nodes),
                  FadeOut(input_face_copy),
                  FadeOut(connects),
                  FadeOut(helping_arrow),
                  FadeOut(helping),
                  FadeOut(helping_text_surround),
                  FadeOut(middles_a),
                  FadeOut(middles),
                  FadeOut(middles_b),
                  FadeOut(outputs))




        pixel_text = TextMobject("Pixel",background_stroke_width=0).move_to(pixel.get_top()+UP)
        self.play(Write(pixel_text))
        r_input = Circle(fill_color="#FF0000", fill_opacity=1, stroke_width=0)
        g_input = Circle(fill_color="#3cff00", fill_opacity=1, stroke_width=0)
        b_input = Circle(fill_color="#0004ff", fill_opacity=1, stroke_width=0)
        color_inputs = VGroup(r_input,g_input,b_input).arrange(RIGHT)
        color_hint_box = SurroundingRectangle(color_inputs,buff=MED_LARGE_BUFF)
        color_hint_text = TextMobject("Každý pixel má tri hodnoty",background_stroke_width=0).move_to(color_hint_box.get_top()+UP/2)
        color_hint = VGroup(color_hint_box,color_hint_text)

        self.play(ReplacementTransform(pixel.copy(),color_inputs))
        self.play(Write(color_hint_box))
        self.play(ReplacementTransform(pixel_text,color_hint_text))
        self.wait()
        self.play(Uncreate(color_hint))
        self.play(ReplacementTransform(color_inputs,pixel))

        r_l = Line(2.5*LEFT,2.5*RIGHT)
        r_t = TextMobject("R").move_to(r_l.get_start()+LEFT/2)
        r_c = Circle(fill_opacity=1, stroke_width=0).scale(0.2).next_to(r_t,LEFT)
        g_l = Line(2.5*LEFT,2.5*RIGHT)
        g_t = TextMobject("G").move_to(g_l.get_start()+LEFT/2)
        g_c = Circle(fill_opacity=1, stroke_width=0).scale(0.2).next_to(g_t,LEFT)
        b_l = Line(2.5*LEFT,2.5*RIGHT)
        b_t = TextMobject("B").move_to(b_l.get_start()+LEFT/2)
        b_c = Circle(fill_opacity=1, stroke_width=0).scale(0.2).next_to(b_t,LEFT)
        r_dot = Dot().move_to(r_l.get_start())
        g_dot = Dot().move_to(g_l.get_start())
        b_dot = Dot().move_to(b_l.get_start())
        r_n = Integer(0).move_to(r_l.get_right()+MED_SMALL_BUFF+DOWN/4)

        g_n = Integer(0).move_to(g_l.get_right()+MED_SMALL_BUFF+DOWN/4)
        b_n = Integer(0).move_to(b_l.get_right()+MED_SMALL_BUFF+DOWN/4)
        r = VGroup(r_c,r_dot,r_l,r_n,r_t)
        g = VGroup(g_c,g_dot,g_l,g_n,g_t)
        b = VGroup(b_c,b_dot,b_l,b_n,b_t)


        colors = VGroup(r,g,b).arrange(DOWN,buff=MED_LARGE_BUFF).to_edge(DOWN)
        colors.move_to(LEFT/2+DOWN*2.7)

        pixel_group = VGroup(pixel,colors)

        r_n.add_updater(lambda d: d.set_value((r_dot.get_center()[0]-r_l.get_start()[0])*51))
        g_n.add_updater(lambda d: d.set_value((g_dot.get_center()[0]-g_l.get_start()[0])*51))
        b_n.add_updater(lambda d: d.set_value((b_dot.get_center()[0]-b_l.get_start()[0])*51))

        pixel.add_updater(lambda d: d.set_fill('#%02x%02x%02x' % (r_n.get_value(), g_n.get_value(), b_n.get_value())))
        r_c.add_updater(lambda d: d.set_fill('#%02x0000' % (r_n.get_value())))
        g_c.add_updater(lambda d: d.set_fill('#00%02x00' % (g_n.get_value())))
        b_c.add_updater(lambda d: d.set_fill('#0000%02x' % (b_n.get_value())))

        start = True
        self.play(Write(colors))
        pixel_text_next = TextMobject("Každý pixel má svoju farbu",background_stroke_width=0).move_to(pixel_text)
        self.play(ReplacementTransform(color_hint_text,pixel_text_next))
        for i in range(2):
            if start:
                self.play(r_dot.move_to,r_l.get_end())
                self.play(g_dot.move_to,g_l.get_end())
                self.play(b_dot.move_to,b_l.get_end())
                start = False
            else:
                self.play(r_dot.move_to,r_l.get_start())
                self.play(g_dot.move_to,g_l.get_start())
                self.play(b_dot.move_to,b_l.get_start())
                start = True

        self.play(pixel.set_fill,"#2A4E83")
        self.wait()



        self.play(Uncreate(colors),Uncreate(pixel_text_next))


        self.play(FadeIn(connects),
                  ReplacementTransform(pixel,inputs[0]),
                  FadeIn(inputs_copy),
                  FadeIn(inputs),
                  FadeIn(nodes),
                  FadeIn(input_face_copy),
                  FadeIn(helping_arrow),
                  FadeIn(helping),
                  FadeIn(helping_text_surround),
                  FadeIn(outputs_copy))



        self.remove(helping_text_next)
        helping_text_next = TextMobject("Sieť zoskupuje pixely", background_stroke_width=0).move_to(helping_text).scale(text_size)
        self.play(Transform(helping_text,helping_text_next))

        self.remove(helping_surround_next)
        self.play(Transform(inputs_copy,middles_a))

        self.remove(helping_text_next)
        helping_text_next = TextMobject("Pixely sa zoskupujú cez ","filtre", background_stroke_width=0).move_to(helping_text).scale(text_size)
        self.play(Transform(helping_text,helping_text_next))








        helping_surround_next = SurroundingRectangle(VGroup(inputs,middles_a), buff=surround_buff, color=WHITE)
        self.play(ReplacementTransform(helping_surround,helping_surround_next))

        self.wait()






        self.play(FadeOut(inputs_copy),
                  FadeOut(inputs),
                  FadeOut(nodes),
                  FadeOut(input_face_copy),
                  FadeOut(connects),
                  FadeOut(helping_arrow),
                  FadeOut(helping[0]),
                  FadeOut(helping_text_surround),
                  FadeOut(middles_a),
                  FadeOut(middles),
                  FadeOut(middles_b),
                  FadeOut(outputs),
                  FadeOut(outputs_copy),
                  FadeOut(helping_surround_next))


        ##Animovat do filtre
        filter_title = TextMobject("Čo robia ","filtre","?",background_stroke_width=0).scale(1.5)
        self.play(Write(filter_title[0]),Write(filter_title[2]),ReplacementTransform(helping_text_next[1],filter_title[1]))
        self.play(Uncreate(helping[1]))
        self.wait()
        self.play(Uncreate(filter_title))
        filter_text = TextMobject("Najprv sa vyhľadávaju základné tvary",background_stroke_width=0)
        filter_text_next = TextMobject("V druhej vrstve spájame základné tvary",background_stroke_width=0)

        filter_one = ImageMobject("filter_one").scale(1)
        filter_two = ImageMobject("filter_two").scale(1)
        filter_three = ImageMobject("filter_three").scale(1)

        filter_text.move_to(filter_one.get_top()+UP)
        filter_text_next.move_to(filter_text)
        self.play(FadeIn(filter_one),ShowPassingFlashAround(filter_one,buff=0),Write(filter_text))
        self.wait()
        self.play(filter_one.move_to,LEFT*3,filter_one.scale,0.9)
        self.play(FadeIn(filter_two),ShowPassingFlashAround(filter_two,buff=0),ReplacementTransform(filter_text,filter_text_next))
        self.wait()
        self.play(filter_two.move_to,RIGHT*4,filter_two.scale,0.9)
        filter_text = TextMobject("V tretej vrstve už dostávame celú tvár",background_stroke_width=0).move_to(filter_text_next)
        self.play(FadeIn(filter_three),ShowPassingFlashAround(filter_three,buff=0),ReplacementTransform(filter_text_next,filter_text))
        self.wait()
        self.play(filter_three.scale,0.9)
        filters = Group(filter_one,filter_two,filter_three)
        filters_copy = filters.copy().arrange(RIGHT,buff=1.1).move_to(RIGHT)
        self.play(ReplacementTransform(filters,filters_copy))
        filter_layer_one = TextMobject("1. vrstva",background_stroke_width=0).move_to(filter_one.get_bottom()+DOWN/4).scale(text_size)
        filter_layer_two = TextMobject("2. vrstva",background_stroke_width=0).move_to(filter_two.get_bottom()+DOWN/4).scale(text_size)
        filter_layer_three = TextMobject("3. vrstva",background_stroke_width=0).move_to(filter_three.get_bottom()+DOWN/4).scale(text_size)
        filters_layer_text = VGroup(filter_layer_one,filter_layer_two,filter_layer_three)
        self.play(FadeInFrom(filters_layer_text,direction=UP))
        filter_onetwo_arrow = Arrow(filter_one.get_right(),filter_two.get_left(),buff=0)
        filter_twothree_arrow = Arrow(filter_two.get_right(),filter_three.get_left(),buff=0)
        filter_arrows = VGroup(filter_onetwo_arrow,filter_twothree_arrow)
        self.play(Write(filter_arrows))


        self.wait()
        self.play(Uncreate(filter_arrows),FadeOut(filters_copy),Uncreate(filters_layer_text),Uncreate(filter_text))



        self.play(FadeIn(connects),
                  FadeIn(inputs_copy),
                  FadeIn(inputs),
                  FadeIn(nodes),
                  FadeIn(input_face_copy),
                  FadeIn(helping_arrow),
                  FadeIn(helping),
                  FadeIn(helping_text_surround),
                  FadeIn(outputs_copy))





        self.remove(helping_surround_next)
        helping_surround_next = SurroundingRectangle(middles_a, buff=surround_buff, color=WHITE)
        self.play(ReplacementTransform(helping_surround,helping_surround_next))
        self.remove(helping_text_next)
        helping_text_next = TextMobject("Aplikujeme filtre", background_stroke_width=0).move_to(helping_text).scale(text_size)
        self.play(Transform(helping_text,helping_text_next))


        self.play(Transform(middles_a_copy,middles))
        self.remove(helping_surround_next)
        helping_surround_next = SurroundingRectangle(VGroup(middles_a,middles), buff=surround_buff, color=WHITE)
        self.play(Transform(helping_surround,helping_surround_next))
        self.wait()

        self.remove(helping_text_next)
        helping_text_next = TextMobject("Dostávame tvár v latentnom priestore", background_stroke_width=0).move_to(helping_text).scale(text_size)
        self.play(Transform(helping_text,helping_text_next))


        self.remove(helping_surround_next)
        helping_surround_next = SurroundingRectangle(middles, buff=surround_buff, color=WHITE)
        self.play(Transform(helping_surround,helping_surround_next))







        ###########################LATENT FACE############################


        latent_square = Square()
        latent_square_image = ImageMobject("latent_face_untrained").move_to(latent_square)
        latent_hint_text = TextMobject("Sieť sa „naučí“ rozpoznať vlastnosi tváre",background_stroke_width=0).move_to(2*UP)
        self.play(ReplacementTransform(middles_a_copy,latent_square),
                  FadeOut(inputs_copy),
                  FadeOut(inputs),
                  FadeOut(nodes),
                  FadeOut(input_face_copy),
                  FadeOut(connects),
                  FadeOut(helping_arrow),
                  FadeOut(helping),
                  FadeOut(helping_text_surround),
                  FadeOut(middles_a),
                  FadeOut(middles),
                  FadeOut(middles_b),
                  FadeOut(outputs),
                  FadeOut(outputs_copy),
                  FadeOut(helping_surround_next),
                  FadeIn(latent_square_image))

        self.play(Write(latent_hint_text))
        self.wait()
        latent_hint_text_next = TextMobject("Tvár sa komprimuje do latentného priestoru",background_stroke_width=0).scale(text_size).move_to(latent_hint_text)
        self.play(ReplacementTransform(latent_hint_text,latent_hint_text_next))
        latent_label = TextMobject("Latentná reprezentácia tváre", background_stroke_width=0).scale(text_size).move_to(latent_square.get_bottom()+DOWN/4)
        self.play(FadeInFrom(latent_label,UP))
        self.wait()
        [self.play(ShowPassingFlash(latent_square)) for i in range(3)]
        self.play(FadeOut(latent_label),FadeOut(latent_square),FadeOut(latent_hint_text_next),FadeOut(latent_square_image))
        self.wait()


        self.play(FadeIn(connects),
                  FadeIn(inputs_copy),
                  FadeIn(inputs),
                  FadeIn(nodes),
                  FadeIn(input_face_copy),
                  FadeIn(helping_arrow),
                  FadeIn(helping),
                  FadeIn(helping_text_surround),
                  FadeIn(outputs_copy))



        #########################NEURAL CONTINUES###############################

        self.play(Transform(middles_copy,middles_b))
        self.remove(helping_surround_next)
        helping_surround_next = SurroundingRectangle(VGroup(middles,middles_b), buff=surround_buff, color=WHITE)
        self.play(Transform(helping_surround,helping_surround_next))
        self.wait()

        self.remove(helping_text_next)
        helping_text_next = TextMobject("Z latentného priestoru sa dekóduje späť", background_stroke_width=0).move_to(helping_text).scale(text_size)
        self.play(Transform(helping_text,helping_text_next))


        self.remove(helping_surround_next)
        helping_surround_next = SurroundingRectangle(middles_b, buff=surround_buff, color=WHITE)
        self.play(Transform(helping_surround,helping_surround_next))

        self.play(Transform(middles_b_copy,outputs_copy))
        self.remove(helping_surround_next)
        helping_surround_next = SurroundingRectangle(VGroup(middles_b,outputs_copy), buff=surround_buff, color=WHITE)
        self.play(Transform(helping_surround,helping_surround_next))
        self.wait()

        self.remove(helping_text_next)
        helping_text_next = TextMobject("Výstup sú pixely a dostávame obrázok s tvárou", background_stroke_width=0).move_to(helping_text).scale(text_size)
        self.play(Transform(helping_text,helping_text_next))
        self.wait()


        self.remove(helping_surround_next)
        helping_surround_next = SurroundingRectangle(outputs, buff=surround_buff, color=WHITE)
        self.play(Transform(helping_surround,helping_surround_next))
        self.wait()


        label = TextMobject("Trénovanie neurónovej sieti", background_stroke_width=0)
        video = Rectangle(height=6.5,width=8.5,fill_color=BLACK,fill_opacity=1)
        label.next_to(video,DOWN)
        grupa = VGroup(video,label)

        self.play(Write(grupa))
        self.wait()
        self.play(FadeOut(grupa))


        self.play(ReplacementTransform(outputs_copy,output_face))

        self.remove(helping_surround_next)
        helping_surround_next = SurroundingRectangle(VGroup(outputs,output_face), buff=surround_buff, color=WHITE)
        self.play(Transform(helping_surround,helping_surround_next))
        self.wait()
        self.remove(helping_surround_next)
        helping_text.clear_updaters()
        helping_arrow.clear_updaters()
        helping_text_surround.clear_updaters()
        self.play(Uncreate(helping_arrow),Uncreate(helping_text),Uncreate(helping_text_surround))
        self.play(Uncreate(helping_text),Uncreate(helping_surround))
        ################################
        self.play(Write(inputs_save))
        ################################
        self.play(FadeIn(output_face_image))
        self.remove(input_face_copy)
        self.remove(output_face_copy)
        self.remove(inputs_copy)
        self.remove(middles_a_copy)
        self.remove(middles_b_copy)
        self.remove(middles_copy)
        self.remove(outputs_copy)



        self.remove(input_face_copy)
        self.remove(output_face_copy)

        ######################### PART III: ENCODER #############################
        #input_face = Square().to_edge(LEFT).scale(0.8)
        #output_face = Square().to_edge(RIGHT).scale(0.8)
        latent_face_abs = Square().scale(0.8)
        encoder_abs = Polygon(UL,UR+DOWN/3,DR+UP/3,DL).scale(0.8)
        decoder_abs = Polygon(UL+DOWN/3,UR,DR,DL+UP/3).scale(0.8)

        encoder_abs.move_to(2.5*LEFT)
        decoder_abs .move_to(2.5*RIGHT)

        #self.play(Write(inputs))


        encoder = VGroup(inputs_save,middles_a)

        self.play(Uncreate(connects),ReplacementTransform(encoder,encoder_abs),ReplacementTransform(decoder,decoder_abs),ReplacementTransform(middles,latent_face_abs))

        self.remove(encoder)
        self.remove(middles)
        self.remove(decoder)
        input_arrow = Arrow(input_face[0].get_right(),encoder.get_left(),buff=0)
        encoder_latent_arrow = Arrow(encoder.get_right(),latent_face_abs.get_left(),buff=0)
        latent_decoder_arrow = Arrow(latent_face_abs.get_right(),decoder.get_left(),buff=0)
        output_arrow = Arrow(decoder.get_right(),output_face[0].get_left(),buff=0)
        arrows = VGroup(input_arrow,encoder_latent_arrow,latent_decoder_arrow,output_arrow)
        self.play(Write(arrows))

        encoder_text = TextMobject("Enkodér",background_stroke_width=0).move_to(encoder_abs.get_bottom()+DOWN/2).scale(text_size)
        latent_text = TextMobject("Latentná Tvár",background_stroke_width=0).move_to(latent_face_abs.get_bottom()+DOWN/2).scale(text_size)
        decoder_text = TextMobject("Dekodér",background_stroke_width=0).move_to(decoder_abs.get_bottom()+DOWN/2).scale(text_size)
        self.play(FadeInFrom(encoder_text,UP),FadeInFrom(latent_text,UP),FadeInFrom(decoder_text,UP))
        self.wait()
        self.play(FadeOutAndShift(encoder_text,UP),FadeOutAndShift(latent_text,UP),FadeOutAndShift(decoder_text,UP))


        self.wait()
        network = VGroup(input_face_box,output_face_box,latent_face_abs,encoder_abs,decoder_abs,arrows)

        network_copy = network.copy()


        input_face_a = TextMobject("Vstupná tvár A", background_stroke_width=0).scale(text_size)
        output_face_a = TextMobject("Rekonštruovaná tvár A", background_stroke_width=0).scale(text_size-0.1)

        input_face_b = TextMobject("Vstupná tvár B", background_stroke_width=0).scale(text_size)
        output_face_b = TextMobject("Rekonštruovaná tvár B", background_stroke_width=0).scale(text_size-0.1)

        output_face_a_a = TextMobject("Rekonštruovaná tvár A", background_stroke_width=0).scale(text_size-0.1)
        output_face_a_b = TextMobject("z tváre B", background_stroke_width=0).scale(text_size)
        output_face_a_r = VGroup(output_face_a_a,output_face_a_b).arrange(DOWN,buff=0.1)

        output_face_b_a = TextMobject("Rekonštruovaná tvár B", background_stroke_width=0).scale(text_size-0.1)
        output_face_b_b = TextMobject("z tváre A", background_stroke_width=0).scale(text_size)
        output_face_b_r = VGroup(output_face_b_a,output_face_b_b).arrange(DOWN,buff=0.1)




        self.play(Uncreate(input_face_label),Uncreate(output_face_label))
        self.play(FadeOut(output_face_image),FadeOut(input_face_image))
        output_arrow.add_updater(lambda d: d.put_start_and_end_on(decoder_abs.get_right(),output_face[0].get_left()))

        self.play(network.move_to,2*UP,network_copy.move_to,2*DOWN)

        input_face_b_image = ImageMobject("input_cage").move_to(network_copy[0][0])
        output_face_b_image = ImageMobject("output_cage").move_to(network_copy[1][0])
        input_face_image.move_to(input_face_box.get_center())
        output_face_image.move_to(output_face_box.get_center())



        self.play(FadeIn(input_face_b_image),FadeIn(output_face_b_image),FadeIn(input_face_image),FadeIn(output_face_image))
        self.play(Write(input_face_a.next_to(input_face_box,DOWN)),Write(output_face_a.next_to(output_face_box,DOWN)),Write(input_face_b.next_to(network_copy[0],DOWN)),Write(output_face_b.next_to(network_copy[1],DOWN)))


        self.wait(2)
        self.play(Uncreate(network_copy[5][2]))

        self.play(FadeOut(output_face_b_image),
                  FadeOut(output_face_image),
                  Uncreate(network_copy[4]),
                  Uncreate(network_copy[1]),
                  Uncreate(network_copy[5][3]),
                  Uncreate(output_face_b),
                  Uncreate(latent_decoder_arrow))

        self.play(decoder_abs.to_edge,DOWN*6.5,buff=2)
        output_face_a.add_updater(lambda d: d.next_to(output_face_box,DOWN))
        self.play(output_face_box.move_to,decoder_abs.get_center()+RIGHT*3)
        combined_face = ImageMobject("output_combined").move_to(output_face_box)
        new_arrow_a = Arrow(decoder_abs.get_right(),output_face_box.get_left(),buff=0)
        new_arrow_b = Arrow(network_copy[2].get_right (),decoder_abs.get_left(),buff=0)
        new_arrow_c = Arrow(latent_face_abs.get_right(),decoder_abs.get_left(),buff=0)
        new_arrows = VGroup(new_arrow_a,new_arrow_b,new_arrow_c)
        self.play(Write(new_arrows),FadeIn(combined_face))

        output_face_a_r.move_to(output_face_a.get_center()+DOWN/3)
        self.play(Uncreate(output_face_a))
        self.play(Write(output_face_a_r))

        self.wait(5)


        #whole_scene = VGroup(network,network_copy,new_arrows)
        #self.wait(2)
        #self.play(Uncreate(whole_scene))
