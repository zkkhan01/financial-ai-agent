def spark_svg(series, width=600, height=180, padding=10):
    if not series: return "<svg/>"
    lo, hi = min(series), max(series)
    span = (hi-lo) or 1.0
    def sx(i): return padding + i*(width-2*padding)/(len(series)-1)
    def sy(v): return height - (padding + (v-lo)*(height-2*padding)/span)
    pts = " ".join(f"{sx(i)},{sy(v)}" for i,v in enumerate(series))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">
  <rect width="100%" height="100%" fill="#0b1020"/>
  <polyline fill="none" stroke="#6cf" stroke-width="2" points="{pts}"/>
</svg>'''
