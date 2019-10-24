def reportline(filename, data):
    reportline = '<p style="margin-left: 0px">'

    reportline += filename
    reportline += ': '

    for line in data:
        line = line.strip('\t').strip('\r').strip('\n').strip('\@').strip('>')

        if len(line.strip(' ')) > 0:
            reportline += line
            reportline += ' | '

    reportline += '</p>\n'
    return reportline