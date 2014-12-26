import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def format(month1, date1, year1, month2, date2, year2, events_string, me, recipient):

  # Create message container - the correct MIME type is multipart/alternative.
  msg = MIMEMultipart('alternative')
  msg['Subject'] = "Department of Philosophy Talks & Events" + "(" + month1 + " " + date1 + " - " + month2 + " " + date2 + ", " + year2 + ")"
  msg['From'] = me
  msg['To'] = recipient


  # Create the body of the message (a plain-text and an HTML version).
  text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
  html1 = """\
  <html><head>
  <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
    </head>
    <body text="#000000" bgcolor="#FFFFFF">
      <div class="moz-text-html" lang="x-western">
        <div class="moz-text-html" lang="x-western">
          <div class="moz-text-html" lang="x-western"> <br>
            <div class="moz-text-html" lang="x-western">
              <blockquote cite="mid:546CC592.3070009@mail.utoronto.ca" type="cite">
                <div class="moz-text-html" lang="x-western">
                  <div class="moz-text-html" lang="x-western"><br>
                    <div class="moz-text-html" lang="x-western">
                      <div class="moz-text-html" lang="x-western">
                        <div class="moz-text-html" lang="x-western">
                          <div class="moz-text-html" lang="x-unicode">
                            <div dir="ltr">
                              <div class="gmail_quote">
                                <div text="#000000" bgcolor="#FFFFFF">
                                  <div>
                                    <div>
                                      <div>
                                        <div>
                                          <div>
                                            <div>
                                              <div>
                                                <div lang="x-western">
                                                  <div lang="x-western">
                                                    <div lang="x-western">
                                                      <div lang="x-western">
                                                        <div lang="x-western">
                                                          <div lang="x-western">
                                                            <div lang="x-western">
                                                            <div lang="x-western">
                                                            <div lang="x-western">
                                                            <div lang="x-western">
                                                            <div lang="x-western">
                                                            <div lang="x-western">
                                                            <div>
                                                            <div>
                                                            <div lang="x-western">
                                                            <blockquote type="cite">
                                                            <div lang="x-western">
                                                            <blockquote type="cite">
                                                            <div lang="x-western">
                                                            <div lang="x-western">
                                                            <div lang="x-western">
                                                            <div lang="x-western">
                                                            <table cellpadding="8" height="453" width="585" border="0">
                                                            <tbody>
                                                            <tr>
                                                            <td rowspan="1" colspan="1" bgcolor="#66ff99"><font face="Calibri" size="6"><b>The
                                                            U of T
                                                            Department of
                                                            Philosophy <br>
                                                            <big><small>Talks
                                                            and Events </small></big></b></font><font face="Calibri" size="6"><b>(""" + month1 + """</b></font><b><font size="6"><font size="6">""" + date1 + ", " + year1 + " " + month2 + " " + date2 + ", " + year2 + """</font></font>)</font></b><font face="Calibri"><br>
                                                            <big>Please
                                                            mark your
                                                            calendars with
                                                            this listing
                                                            of talks and
                                                            events in the
                                                            Department.
                                                            Also, </big></font><big><font face="Calibri">visit
                                                            </font></big><big><font face="Calibri"><a moz-do-not-send="true" href="http://www.philosophy.utoronto.ca/events/" target="_blank">http://www.philosophy.utoronto.ca/events/</a> </font></big><big><font face="Calibri">for
                                                            a complete
                                                            listing of
                                                            upcoming talks
                                                            and events. </font></big></td>
                                                            </tr>"""
  html2 = """\
                                                            </tbody>
                                                            </table>
                                                            </div>
                                                            </div>
                                                            </div>
                                                            </div>
                                                            </blockquote>
                                                            </div>
                                                            </blockquote>
                                                            </div>
                                                            </div>
                                                            </div>
                                                            </div>
                                                            </div>
                                                            </div>
                                                            </div>
                                                            </div>
                                                            </div>
                                                          </div>
                                                        </div>
                                                      </div>
                                                    </div>
                                                  </div>
                                                </div>
                                              </div>
                                            </div>
                                          </div>
                                        </div>
                                      </div>
                                    </div>
                                  </div>
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </blockquote>
            </div>
          </div>
        </div>
      </div>
    </body>
  </html>"""

  html = html1 + events_string + html2

  # Record the MIME types of both parts - text/plain and text/html.
  part1 = MIMEText(text, 'plain')
  part2 = MIMEText(html, 'html')

  # Attach parts into message container.
  # According to RFC 2046, the last part of a multipart message, in this case
  # the HTML message, is best and preferred.
  msg.attach(part1)
  msg.attach(part2)

  # Send the message via gmail
  s = smtplib.SMTP('smtp.gmail.com', 587)
  s.starttls()
  s.ehlo()
  s.login(me, "shhhhsecret!")

  # sendmail function takes 3 arguments: sender's address, recipient's address
  # and message to send - here it is sent as one string.
  s.sendmail(me, recipient, msg.as_string())
  s.quit()
  return ("Success! Internal Omnibus Sent! Check your email! Whooo!")
