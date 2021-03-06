def get_mail_content(name, title):
    content = f"""
<div id="doc" class="markdown-body container-fluid comment-inner comment-enabled" data-hard-breaks="true"><p><span>Dear {name},</span>
</p>
    <p><span>I am Shirley from PyCon Taiwan 2021 program committee. Thank you for submitting your proposal to PyCon Taiwan 2021. Your proposal ā{title}ā is ACCEPTED by PyCon Taiwan 2021. Iām writing this letter to confirm your willingness to be our speaker. We are happy to invite you to speak at PyCon Taiwan 2021 and we appreciate all your support.</span>
    </p>
    <p><span>Due to the rise of COVID-19 cases in Taiwan, this year, we decided to hold PyCon TW virtually and the date would be postponed until October 2nd (Sat) and 3rd (Sun). Please let us know before July 7th:</span>
    </p>
    <ol>
        <li><span>Whether you are able to attend the event</span></li>
        <li><span>Your virtual speech preference</span><br>
            <span>a. Pre-recorded speech plus a 5 - 10 minutes Q&amp;A section live stream</span><br>
            <span>b. Full-time live stream</span></li>
    </ol>
    <p><span>We will confirm the details of your presentation, such as the presentation time, and provide you with the exclusive ticket code (Everybody Contributes is one of the core principles of PyCon. All attendees including speakers, chairperson, staff, and volunteers have to pay for registering)  after your reply.</span>
    </p>
    <p><span>Last but not least, PyCon Taiwan has announced its Financial Aid Program, which is for anyone who needs financial support to join PyCon TW 2021. You can find more details from the </span><a
            href="https://tw.pycon.org/2021/en-us/registration/financial-aid" target="_blank" rel="noopener"><span>Financial Aid Program</span></a><span> if needed. (The new deadline of the program is until August 1st; information on the official website would be updated soon.)</span>
    </p>
    <p><span>Looking forward to hearing from you before July 7th. Thank you again for your contribution to PyCon Taiwan and the Python community as a whole!</span>
    </p>
    <p><span>If you have any questions, please feel free to contact us through </span><a href="mailto:program@pycon.tw"
                                                                                         target="_blank" rel="noopener"><span>program@pycon.tw</span></a><span>.</span>
    </p>
    <p><span>č¦Ŗęē {name},</span></p>
    <p><span>ęęÆ PyCon Taiwan 2021 č­°ēØēµē Shirleyļ¼ęč¬ęØå PyCon Taiwan 2021 ęēØæęØēēØæä»¶ćęØēēØæä»¶ ā{title}ā å·²č¢« PyCon Taiwan 2021 éåļ¼ęåę³åęØē¢ŗčŖęä»» PyCon Taiwan 2021 ēč¬čęé”ļ¼ęåå¾ę¦®å¹øéč«ęØåå  PyCon Taiwan 2021 ęä»»č¬čļ¼äø¦ęč¬ęØēŗę­¤ę¬”ę“»åęä¾ēęęęÆęčåå©ć</span>
    </p>
    <p><span>å ęå°ē£ē«ęéę¼øåęŗ«ļ¼ęåä»å¹“å°ä»„åØē·äøēå½¢å¼čč¾¦ PyCon TWļ¼äø¦å°ę„ęå»¶å¾č³ 10 / 2 (å­)ć10 / 3 (ę„)ćč«ę¼ 7 / 7 (äø) åč®ęåē„é</span></p>
    <ol>
        <li><span>ęØęÆå¦č½å¤ ęä»»ę¬ę¬”å¤§ęēč¬čć</span></li>
        <li><span>å¦ęęØč½å¤ åčļ¼ęØåå„½ēę¼č¬ę¹å¼ēŗļ¼</span><br>
            <span>a. é åéå½±: é éęØę¼č¬åå„½é·åŗ¦ēå½±ē + 5 ~ 10 åéē“ę­ Q&amp;A</span><br>
            <span>b. ē·äøē“ę­: åØēØē·äøē“ę­ę¼č¬</span></li>
    </ol>
    <p><span>å¾ęØåč¦å¾ļ¼ęåå°ęčęØčÆē¹«čē¢ŗčŖę¼č¬ēēøéē“°ēÆļ¼ä¾å¦ę¼č¬ęéå®ęćęä¾ēµ¦ęØå°å±¬ēč¬čč³¼ē„Øä»£ē¢¼ļ¼PyCon TW ē§ę Everybody Contributes ååļ¼ęęēęč­°åččļ¼å¦ļ¼č¬čćęč­°äø»åø­ćå·„ä½äŗŗå”ćåæå·„ļ¼ēéčŖå·±ä»č²»ļ¼ć</span>
    </p>
    <p><span>é¤ę­¤ä¹å¤ļ¼å¦ęęØéč¦ä»»ä½ēč²”åäøēåå©ļ¼ä¹čŖ ęÆę­”čæęØē³č«ä»å¹“č²”åč£å©ę¹ę”ćåŖč¦ęØęåŗéę±ļ¼PyCon TW é½ęē”åÆč½åå©ęØćå¦ęéč¦ļ¼č«å°</span><a
            href="https://tw.pycon.org/2021/zh-hant/registration/financial-aid" target="_blank" rel="noopener"><span>č²”åč£å©é é¢</span></a><span>č¦č©³ē“°ē³č«č¾¦ę³ćļ¼ä»å¹“č²”åč£å©ęéå°å»¶é·č³ 8 / 1 ļ¼čæęęę“ę°ę„ęč³å®ē¶²č³čØļ¼</span>
    </p>
    <p><span>ęååøęč½åØ 7 / 7 (äø) ä¹åę¶å°ęØēåč¦ļ¼åę¬”ęč¬ęØå° PyCon Taiwan ä»„å Python ē¤¾ē¾¤ēč²¢ē»ļ¼</span></p>
    <p><span>å¦ęęØęä»»ä½ēåļ¼ä¹ę­”čæęØä¾äæ” </span><a href="mailto:program@pycon.tw" target="_blank" rel="noopener"><span>program@pycon.tw</span></a><span> čęåčÆē¹«ć</span>
    </p>
    <p><span>Best Regards,</span><br>
        <span>Shirley Lin</span><br>
        <span>PyCon Taiwan 2021 Program Committee</span></p></div>
    """

    return content
