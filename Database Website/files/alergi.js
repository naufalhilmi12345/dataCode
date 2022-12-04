$(document).ready(function() {
    var angka = 1;
    $('#tambah').click(function() {
        var fix = `<input type="text" name="alergi-` + angka + `" maxlength="50" required id="id_alergi-` + angka + `">`
        $('.alergi').append(fix);
        angka++;
    })
    $('#kurang').click(function() {
        if (angka > 1) {
            angka--;
            $('#id_alergi-' + angka).remove();
        } else {
            alert('gkboleh cuy');
        }
    })
})