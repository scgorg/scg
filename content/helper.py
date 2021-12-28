def get_mail_content(name, title):
    content = f"""
<div id="doc" class="markdown-body container-fluid comment-inner comment-enabled" data-hard-breaks="true"><p><span>Dear {name},</span>
</p>
    <p><span>I am Shirley from PyCon Taiwan 2021 program committee. Thank you for submitting your proposal to PyCon Taiwan 2021. Your proposal “{title}” is ACCEPTED by PyCon Taiwan 2021. I’m writing this letter to confirm your willingness to be our speaker. We are happy to invite you to speak at PyCon Taiwan 2021 and we appreciate all your support.</span>
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
    <p><span>親愛的 {name},</span></p>
    <p><span>我是 PyCon Taiwan 2021 議程組的 Shirley，感謝您向 PyCon Taiwan 2021 投稿您的稿件。您的稿件 “{title}” 已被 PyCon Taiwan 2021 錄取，我們想和您確認擔任 PyCon Taiwan 2021 的講者意願，我們很榮幸邀請您參加 PyCon Taiwan 2021 擔任講者，並感謝您為此次活動提供的所有支持與協助。</span>
    </p>
    <p><span>因應台灣疫情逐漸升溫，我們今年將以全線上的形式舉辦 PyCon TW，並將日期延後至 10 / 2 (六)、10 / 3 (日)。請於 7 / 7 (三) 前讓我們知道</span></p>
    <ol>
        <li><span>您是否能夠擔任本次大會的講者。</span></li>
        <li><span>如果您能夠參與，您偏好的演講方式為：</span><br>
            <span>a. 預先錄影: 預錄您演講偏好長度的影片 + 5 ~ 10 分鐘直播 Q&amp;A</span><br>
            <span>b. 線上直播: 全程線上直播演講</span></li>
    </ol>
    <p><span>待您回覆後，我們將會與您聯繫與確認演講的相關細節，例如演講時間安排、提供給您專屬的講者購票代碼（PyCon TW 秉持 Everybody Contributes 原則，所有的會議參與者，如：講者、會議主席、工作人員、志工，皆需自己付費）。</span>
    </p>
    <p><span>除此之外，如果您需要任何的財務上的協助，也誠摯歡迎您申請今年財務補助方案。只要您提出需求，PyCon TW 都會盡可能協助您。如有需要，請到</span><a
            href="https://tw.pycon.org/2021/zh-hant/registration/financial-aid" target="_blank" rel="noopener"><span>財務補助頁面</span></a><span>見詳細申請辦法。（今年財務補助期限將延長至 8 / 1 ，近期會更新日期至官網資訊）</span>
    </p>
    <p><span>我們希望能在 7 / 7 (三) 之前收到您的回覆，再次感謝您對 PyCon Taiwan 以及 Python 社群的貢獻！</span></p>
    <p><span>如果您有任何疑問，也歡迎您來信 </span><a href="mailto:program@pycon.tw" target="_blank" rel="noopener"><span>program@pycon.tw</span></a><span> 與我們聯繫。</span>
    </p>
    <p><span>Best Regards,</span><br>
        <span>Shirley Lin</span><br>
        <span>PyCon Taiwan 2021 Program Committee</span></p></div>
    """

    return content
