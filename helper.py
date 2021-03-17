def get_mail_content(name):
    content = f"""
<div id="doc" class="markdown-body container-fluid comment-inner comment-enabled" data-hard-breaks="true">
  <p><span>Dear {name},</span></p>
  <p><span>This is JunWei from PyCon Taiwan. Thank you for submitting your proposals to PyCon Taiwan in the past, PyCon Taiwan will take place August 20 - August 22, 2021, in Taipei + Virtually, we would be pleased to welcome you to celebrate the
      10th anniversary of PyCon Taiwan together.</span></p>
  <p><span>The Call for Proposals is open now. We accept 15, 30, or 45 minutes for talks and 1.5 hours for tutorials, all topics are welcome. If you’re interested in presenting your innovative ideas at this year’s event, please submit your proposal
      by April 26, 2021.</span></p>
  <p><span>Due to the ongoing global pandemic, PyCon Taiwan 2021 will be run in a “hybrid way”. As speakers, you can choose either to present remotely or in-person. Our online attendees, including online speakers, can also join our Discord to
      interact with others and watch talks via live stream. Unlike common online events, you will be able to see and interact with the audience in the venue. This kind of experience received good feedback from our keynote speaker last year. On top of
      our semi-hybrid experience, we’ll try our best to make attending online as fun as attending in-person.</span></p>
  <p><span>Talks &amp; Tutorial CFP ends: April 26, 23:59:59 (</span><a href="https://www.timeanddate.com/worldclock/converter.html?iso=20210427T115900&amp;p1=tz_aoe&amp;p2=241&amp;p3=1440" target="_blank"
      rel="noopener"><span>AoE</span></a><span>)</span><br>
    <span>For more information about our conference, please visit </span><a href="https://tw.pycon.org/en-us/speaking/cfp" target="_blank" rel="noopener"><span>https://tw.pycon.org/en-us/speaking/cfp</span></a>
  </p>
  <p><span>We’re looking forward to your proposals :)</span></p>
  <p><span>親愛的 {name} 您好</span></p>
  <p><span>我是 PyCon Taiwan 2021 議程組的駿瑋，感謝您過去曾向 PyCon Taiwan 投遞稿件，今年的 PyCon Taiwan 將於 2021 年 8 月 20 日至 8 月 22 日於台北舉辦實體/線上會議，歡迎您一同參與此次 PyCon Taiwan 十周年的盛會。</span></p>
  <p><span>目前投稿系統已正式開放，您可以投稿長度為 15 分鐘、 30 分鐘或 45 分鐘的議程(talk)，以及 1.5 小時的課程(tutorial)，稿件主題不限。如果您有興趣在今年的活動中分享您的創新想法，歡迎您於 2021 年 4 月 26 日之前提交您的稿件。</span></p>
  <p><span>由於全球的疫情影響，PyCon Taiwan 2021 將以 實體/線上 同步進行，作為講者，您可以選擇遠端演講或親自參加。PyCon Taiwan 的線上參與者(包括遠端講者)均可加入到 PyCon Taiwan 的 Discord，與觀眾互動並通過直播觀看整個議程。有別於單純的線上活動，您將可在會場中看到觀眾並與觀眾互動，這樣的體驗在去年我們獲得來自 Keynote
      講者給予良好的回饋。除了實體研討會的體驗之外，我們將會盡最大努力使線上參加與親自參與一樣有趣。</span></p>
  <p><span>議程、課程 投稿截止：4 月 26 日 23:59:59 (</span><a href="https://www.timeanddate.com/worldclock/converter.html?iso=20210427T115900&amp;p1=tz_aoe&amp;p2=241&amp;p3=1440" target="_blank" rel="noopener"><span>AoE</span></a><span>)</span><br>
    <span>有關大會的更多資訊，請參考 </span><a href="https://tw.pycon.org/zh-hant/speaking/cfp" target="_blank" rel="noopener"><span>https://tw.pycon.org/zh-hant/speaking/cfp</span></a>
  </p>
  <p><span>我們期待您再次投稿 :)</span></p>
  <p><span>Warm Regards,</span><br>
    <span>JunWei Song</span><br>
    <span>PyCon Taiwan 2021 Program Committee</span>
  </p>
</div>
    """

    return content
