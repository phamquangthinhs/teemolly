print ("Hay nhap du lieu o trong dau '' nhe")
dt1 = input ('Hay nhap url cua platform : \n')
dt2 = input ('Hay nhap ten cua chiec ao nay: \n')
dt3 = input ('Cai ao nay bn $ ay nhi? 21.99$ ha? \n')
dt4 = input ('Hay nhap url anh 1140x400 pixel : \n')
dt5 = input ('Hay nhap ten cho pixel theo goi \n')
ct1 = """<div class="gia">"""
ct2 = """</div>
<!--more-->
<div class="tm13">
<div class="container">
<div class="row">
<div class="col-lg-12 col-md-12 col-xs-12">
<div class="tn1">
<ul>
 	<li><a href="http://teemolly.com/?page_id=69">Fishing</a></li>
 	<li><a href="http://teemolly.com/?page_id=107">Jobs</a></li>
 	<li><a href="http://teemolly.com/?page_id=113">Gym </a></li>
 	<li><a href="http://teemolly.com/?page_id=115">Family</a></li>
 	<li><a href="http://teemolly.com/?page_id=119">Yoga</a></li>
 	<li><a href="http://teemolly.com/?page_id=123">Pets</a></li>
 	<li><a href="http://teemolly.com/?page_id=127">Sports</a></li>
 	<li><a href="http://teemolly.com/?page_id=129">MISC</a></li>
</ul>
</div>
</div>
</div>
</div>
</div>
<div class="container">
<div class="row">
<div class="col-lg-12 col-md-12 col-xs-12">
<div class="tm14">
<ul>
 	<li><a href="#.">Production</a></li>
 	<li><a href="#.">Maket</a></li>
</ul>
</div>
<div class="tm15">"""
ct3 = """</div>
<div class="tm16"><img src=\""""
ct4 = """" alt="" /></div>
</div>
</div>
<div class="row">
<div class="col-lg-2 col-md-2 col-xs-4">
<div class="tm17">
<div class="tn1">
<ul>
 	<li>Only</li>
 	<li>"""
ct5 = """</li>
</ul>
</div>
</div>
</div>
<div class="col-lg-5 col-md-5 col-xs-8">
<div class="tm18">
<div class="tn1">

Want to find out more information and buy it, click on "Buy it now" you will be redirected to another site (<a href="http://teemolly.com/?page_id=16">Why?</a>)

</div>
<div class="tn2"><a href=\""""
ct6 = """">Buy It Now</a></div>
</div>
</div>
<div class="col-lg-4 col-md-4 col-xs-10 col-lg-offet-1 col-md-offset-1 col-xs-offset-1">
<div class="tm19">
<div class="tn1">Share this design!</div>
<div class="tn2"><a href="javascript:fbshareCurrentPage()" target="_blank">Facebook</a></div>
<div class="tn2 tn3"><a target="_blank">Twitter</a></div>
</div>
</div>
</div>
</div>
<script>
fbq('track', 'ViewContent', {
            content_type: 'Product',
            content_name: '"""
ct7 = """'
        });
</script>
<div class="tm20"></div>"""
tt = open('output.html','w')
code = ct1 + dt3 + ct2 + dt2 + ct3 + dt4 + ct4 + dt3 + ct5 + dt1 + ct6 + dt5 + ct7
tt.write(code)
print ('Done !')
