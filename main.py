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


# Determine which ASCII art to display based on date
def display_zodiac_art(month, day):
    if (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return capricorn_ascii()
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return aquarius_ascii()
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return pisces_ascii()
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return aries_ascii()
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return taurus_ascii()
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return gemini_ascii()
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return cancer_ascii()
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return leo_ascii()
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return virgo_ascii()
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return libra_ascii()
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return scorpio_ascii()
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return sagittarius_ascii()


# Route to display zodiac ASCII art
@app.route('/')
def zodiac():
    date_str = request.args.get('date', None)

    if date_str:
        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            month = date_obj.month
            day = date_obj.day
            result = display_zodiac_art(month, day)
        except ValueError:
            result = "Invalid date format. Please use YYYY-MM-DD."
    else:
        result = "Please provide a date in the URL, e.g., /?date=2024-07-15"

    # Load index.html from the root directory
    with open('index.html') as file:
        template = file.read()

    # Use render_template_string to render the HTML directly
    return render_template_string(template, result=result)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)