import pygame

class ScoreBoard:
    score=0
    time=0

    
    @staticmethod
    def init_ScoreBoard(rectangle=pygame.rect.Rect(0,50,200,50),textSize=100,textColor=(50,70,100)):
        ScoreBoard.textSize=textSize
        ScoreBoard.textColor=textColor
        ScoreBoard.rectangle=rectangle
        ScoreBoard.score = 100
        ScoreBoard.textSizee = textSize
        ScoreBoard.textColorr = textColor
        ScoreBoard.rectanglee = rectangle
        ScoreBoard.scoree = 100
        
        

    @staticmethod
    def set_Fuel(score=100):
        ScoreBoard.score -= 1
        ScoreBoard.score_fontedText = pygame.font.Font("fonts/ARCADE.TTF", ScoreBoard.textSize).render(
            str(ScoreBoard.score), True, ScoreBoard.textColor)
        ScoreBoard.score_textRectangle = pygame.rect.Rect(0, 0, ScoreBoard.score_fontedText.get_width(),
                                                          ScoreBoard.score_fontedText.get_height()-200)
        ScoreBoard.score_textRectangle.center = ScoreBoard.rectangle.center

    @staticmethod
    def set_Score(score=0):
        ScoreBoard.scoree += 1
        
        ScoreBoard.score_fontedTextt = pygame.font.Font("fonts/ARCADE.TTF", ScoreBoard.textSizee).render(
            str(ScoreBoard.scoree), True, ScoreBoard.textColorr)
        ScoreBoard.score_textRectanglee = pygame.rect.Rect(0, 0, ScoreBoard.score_fontedTextt.get_width(),
                                                           ScoreBoard.score_fontedTextt.get_height())
        ScoreBoard.score_textRectanglee.center = ScoreBoard.rectangle.center

    
    
    @staticmethod
    def draw(screen):
        screen.blit(ScoreBoard.score_fontedText,ScoreBoard.score_textRectangle)
        screen.blit(ScoreBoard.score_fontedTextt, ScoreBoard.score_textRectanglee)


