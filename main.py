from flask import Flask, request, render_template_string
from datetime import datetime


app = Flask(__name__)



def capricorn_ascii():
    return """                  *<br>
             *<br>"""


def aquarius_ascii():
    return """          *** *<br>
       * *   *   *<br>
       *  *   *       *<br>
      * *   <br>"""


def pisces_ascii():
    return """         *<br>
        * *<br>
         *<br>
        *<br>
       *             *<br>
      *  *   * *  * *  *<br>
                     *<br>"""


def aries_ascii():
    return """         *   <br>
              *<br>
                 *<br>
                  *<br>"""


def taurus_ascii():
    return """            *   <br>
       *        *<br>
                  *   <br>
                *  *   <br>
                  * *   <br>
                     *   <br>
                          *     * <br>
                        *         * <br>
                           *   <br>"""


def gemini_ascii():
    return """           *   <br>
       *      *<br>
      *          <br>
                  *   <br>
              *     *      *  *<br>
                   *   <br>
                      *   <br>
                  *   <br>"""


def cancer_ascii():
    return """   *   <br>
    *   <br>
    *   <br>
  *      *   <br>"""


def leo_ascii():
    return """              *   <br>
          *    *   <br>
   *      *   <br>
              *   <br>
                   <br>
*    *         *   <br>"""


def virgo_ascii():
    return """         *   <br>
  *        *         *   <br>
     *      *   *   *<br>
   *   <br>"""


def libra_ascii():
    return """     *   <br>
  *       *   <br>
              <br>
           * <br>
   *   <br>"""


def scorpio_ascii():
    return """                *   <br>
           *     *   <br>
          *     *   <br>
                *   <br>
 * *      *   <br>
*        *   <br>
  *  *  *   <br>"""


def sagittarius_ascii():
    return """              *    *<br>
             *    * <br>
               *    *  <br>
              *   <br>
                   <br>
  *  *  *     *   <br>
       *           *   <br>"""

# Add this dictionary to your main.py file
zodiac_descriptions = {
    "Capricorn": "Capricorn is known for being responsible, disciplined, and self-controlled.",
    "Aquarius": "Aquarius is known for being innovative, original, and independent.",
    "Pisces": "Pisces is known for being compassionate, artistic, and intuitive.",
    "Aries": "Aries is known for being adventurous, energetic, and courageous.",
    "Taurus": "Taurus is known for being reliable, patient, and practical.",
    "Gemini": "Gemini is known for being adaptable, outgoing, and intelligent.",
    "Cancer": "Cancer is known for being emotional, nurturing, and intuitive.",
    "Leo": "Leo is known for being confident, ambitious, and generous.",
    "Virgo": "Virgo is known for being analytical, meticulous, and practical.",
    "Libra": "Libra is known for being diplomatic, charming, and social.",
    "Scorpio": "Scorpio is known for being passionate, resourceful, and determined.",
    "Sagittarius": "Sagittarius is known for being optimistic, adventurous, and enthusiastic."
}



# Determine which ASCII art to display based on date
def display_zodiac_art(month, day):
    zodiac_sign = ""
    ascii_art = ""

    if (month == 12 and day >= 22) or (month == 1 and day <= 19):
        zodiac_sign = "Capricorn"
        ascii_art = capricorn_ascii()
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        zodiac_sign = "Aquarius"
        ascii_art = aquarius_ascii()
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        zodiac_sign = "Pisces"
        ascii_art = pisces_ascii()
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        zodiac_sign = "Aries"
        ascii_art = aries_ascii()
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        zodiac_sign = "Taurus"
        ascii_art = taurus_ascii()
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        zodiac_sign = "Gemini"
        ascii_art = gemini_ascii()
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        zodiac_sign = "Cancer"
        ascii_art = cancer_ascii()
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        zodiac_sign = "Leo"
        ascii_art = leo_ascii()
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        zodiac_sign = "Virgo"
        ascii_art = virgo_ascii()
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        zodiac_sign = "Libra"
        ascii_art = libra_ascii()
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        zodiac_sign = "Scorpio"
        ascii_art = scorpio_ascii()
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        zodiac_sign = "Sagittarius"
        ascii_art = sagittarius_ascii()

    return ascii_art, zodiac_sign



# Route to display zodiac ASCII art
@app.route('/')
def zodiac():
    date_str = request.args.get('date', None)

    if date_str:
        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            month = date_obj.month
            day = date_obj.day
            result, zodiac_sign = display_zodiac_art(month, day)
            description = zodiac_descriptions[zodiac_sign] if zodiac_sign else ""
        except ValueError:
            result = "Invalid date format. Please use YYYY-MM-DD."
            description = ""
    else:
        result = "Please provide a date in the URL, e.g., /?date=2024-07-15"
        description = ""

    with open('index.html') as file:
        template = file.read()

    return render_template_string(template, result=result, description=description)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)