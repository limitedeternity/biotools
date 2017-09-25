/*jshint esversion: 6 */

$(document).ready(function() {
    $("#input").on("submit", function(a) {
        if (navigator.onLine) {
            a.preventDefault();

            $("#output").show();
            $("#data-output").html('<div class="span"><div class="typing_loader"></div></div>');
            
            var csrf_token = "{{ csrf_token() }}";
            $.ajaxSetup({
                beforeSend: function(xhr, settings) {
                    if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", csrf_token);
                    }
                }
            });

            $.ajax({
                url: "/webapp",
                type: "POST",
                dataType: "json",
                data: $("#input").serialize(),
            })
            .done(function(data) {
                $("#data-output").html(data);
            })
            .fail(function() {
                $("#data-output").html("<ul><li>Error occured. Please reload page and try again.</li></ul>");
            });
            
        } else {
            a.preventDefault();
            var data = $("#input").serializeArray().reduce(function(obj, item) {
                obj[item.name] = item.value;
                return obj;
            }, {});

            if (data.seq_in != null && data.action != null) {
                var sequence = data.seq_in.trim().toUpperCase();
                var action = data.action;

                var dna_protein_table = {
                    "ATA": "I",
                    "ATC": "I",
                    "ATT": "I",
                    "ATG": "M",
                    "ACA": "T",
                    "ACC": "T",
                    "ACG": "T",
                    "ACT": "T",
                    "AAC": "N",
                    "AAT": "N",
                    "AAA": "K",
                    "AAG": "K",
                    "AGC": "S",
                    "AGT": "S",
                    "AGA": "R",
                    "AGG": "R",
                    "CTA": "L",
                    "CTC": "L",
                    "CTG": "L",
                    "CTT": "L",
                    "CCA": "P",
                    "CCC": "P",
                    "CCG": "P",
                    "CCT": "P",
                    "CAC": "H",
                    "CAT": "H",
                    "CAA": "Q",
                    "CAG": "Q",
                    "CGA": "R",
                    "CGC": "R",
                    "CGG": "R",
                    "CGT": "R",
                    "GTA": "V",
                    "GTC": "V",
                    "GTG": "V",
                    "GTT": "V",
                    "GCA": "A",
                    "GCC": "A",
                    "GCG": "A",
                    "GCT": "A",
                    "GAC": "D",
                    "GAT": "D",
                    "GAA": "E",
                    "GAG": "E",
                    "GGA": "G",
                    "GGC": "G",
                    "GGG": "G",
                    "GGT": "G",
                    "TCA": "S",
                    "TCC": "S",
                    "TCG": "S",
                    "TCT": "S",
                    "TTC": "F",
                    "TTT": "F",
                    "TTA": "L",
                    "TTG": "L",
                    "TAC": "Y",
                    "TAT": "Y",
                    "TAA": "*",
                    "TAG": "*",
                    "TGC": "C",
                    "TGT": "C",
                    "TGA": "*",
                    "TGG": "W",
                };

                var rna_protein_table = {
                    "UUU": "F",
                    "UUC": "F",
                    "UUA": "L",
                    "UUG": "L",
                    "UCU": "S",
                    "UCC": "s",
                    "UCA": "S",
                    "UCG": "S",
                    "UAU": "Y",
                    "UAC": "Y",
                    "UAA": "*",
                    "UAG": "*",
                    "UGU": "C",
                    "UGC": "C",
                    "UGA": "*",
                    "UGG": "W",
                    "CUU": "L",
                    "CUC": "L",
                    "CUA": "L",
                    "CUG": "L",
                    "CCU": "P",
                    "CCC": "P",
                    "CCA": "P",
                    "CCG": "P",
                    "CAU": "H",
                    "CAC": "H",
                    "CAA": "Q",
                    "CAG": "Q",
                    "CGU": "R",
                    "CGC": "R",
                    "CGA": "R",
                    "CGG": "R",
                    "AUU": "I",
                    "AUC": "I",
                    "AUA": "I",
                    "AUG": "M",
                    "ACU": "T",
                    "ACC": "T",
                    "ACA": "T",
                    "ACG": "T",
                    "AAU": "N",
                    "AAC": "N",
                    "AAA": "K",
                    "AAG": "K",
                    "AGU": "S",
                    "AGC": "S",
                    "AGA": "R",
                    "AGG": "R",
                    "GUU": "V",
                    "GUC": "V",
                    "GUA": "V",
                    "GUG": "V",
                    "GCU": "A",
                    "GCC": "A",
                    "GCA": "A",
                    "GCG": "A",
                    "GAU": "D",
                    "GAC": "D",
                    "GAA": "E",
                    "GAG": "E",
                    "GGU": "G",
                    "GGC": "G",
                    "GGA": "G",
                    "GGG": "G",
                };

                var nucleotide_mass_table = {
                    "A": 135.013,
                    "C": 111.1,
                    "G": 151.13,
                    "T": 126.1133,
                    "U": 112.0868,
                };

                var protein_mass_table = {
                    "A": 89.09,
                    "B": 132.1179,
                    "C": 132.12,
                    "D": 133.11,
                    "E": 147.13,
                    "F": 165.19,
                    "G": 75.0666,
                    "H": 155.1546,
                    "I": 131.1729,
                    "K": 146.19,
                    "L": 131.17,
                    "M": 149.21,
                    "N": 132.1179,
                    "P": 115.13,
                    "Q": 146.14,
                    "R": 174.2,
                    "S": 105.09,
                    "T": 119.1192,
                    "V": 117.151,
                    "W": 204.225,
                    "Y": 181.19,
                    "Z": 146.14,
                    "*": 0.000,
                };

                var dna_complementation = {
                    "A": "T",
                    "T": "A",
                    "G": "C",
                    "C": "G",
                };

                var rna_complementation = {
                    "T": "A",
                    "A": "U",
                    "U": "A",
                    "G": "C",
                    "C": "G",
                };

                var reverse_rna_complementation = {
                    "U": "A",
                    "A": "T",
                    "G": "C",
                    "C": "G",
                };

                var water = 18.01;

                if (action == "DNA to protein") {
                    var result = sequence.replace(/[AGTC]{3}/g, m => dna_protein_table[m]);
                    $("#output").show();
                    $("#data-output").html("<input type='text' value='" + result + "' name='seq_out' autocomplete='off' />");

                } else if (action == "DNA to m-RNA") {
                    var result = sequence.replaceAll("T", "U");
                    $("#output").show();
                    $("#data-output").html("<input type='text' value='" + result + "' name='seq_out' autocomplete='off' />");

                } else if (action == "DNA to t-RNA" || action == "t-RNA to m-RNA" || action == "m-RNA to t-RNA") {
                    var arr = sequence.split('');
                    for (var i = 0; i < arr.length; i++) {
                        arr[i] = rna_complementation[arr[i]];
                    }

                    var result = arr.join('');
                    $("#output").show();
                    $("#data-output").html("<input type='text' value='" + result + "' name='seq_out' autocomplete='off' />");

                } else if (action == "DNA complement") {
                    var arr = sequence.split('');
                    for (var i = 0; i < arr.length; i++) {
                        arr[i] = dna_complementation[arr[i]];
                    }

                    var result = arr.join('');
                    $("#output").show();
                    $("#data-output").html("<input type='text' value='" + result + "' name='seq_out' autocomplete='off' />");

                } else if (action == "Reverse sequence") {
                    var result = sequence.split('').reverse().join('');
                    $("#output").show();
                    $("#data-output").html("<input type='text' value='" + result + "' name='seq_out' autocomplete='off' />");

                } else if (action == "RNA nucleotides count" || action == "DNA nucleotides count") {
                    var count = sequence.match(/[AGTUC]{1}/g).reduce(function(memo, character) {
                        memo[character] = memo[character] + 1 || 1;
                        return memo;
                    }, {});

                    var result = JSON.stringify(count).replaceAll('{', '').replaceAll('}', '').replaceAll('"', '').replaceAll(':', ' - ').replaceAll(',', ', ');
                    $("#output").show();
                    $("#data-output").html("<ul><li>" + result + "</li></ul>");

                } else if (action == "DNA trinucleotides count" || action == "RNA trinucleotides count") {
                    var count = sequence.match(/[AGTUC]{3}/g).reduce(function(memo, bundle) {
                        memo[bundle] = memo[bundle] + 1 || 1;
                        return memo;
                    }, {});

                    var result = JSON.stringify(count).replaceAll('{', '').replaceAll('}', '').replaceAll('"', '').replaceAll(':', ' - ').replaceAll(',', ', ');
                    $("#output").show();
                    $("#data-output").html("<input type='text' value='" + result + "' name='seq_out' autocomplete='off' />");

                } else if (action == "Aminoacids count") {
                    var count = sequence.split('').reduce(function(memo, character) {
                        memo[character] = memo[character] + 1 || 1;
                        return memo;
                    }, {});

                    var result = JSON.stringify(count).replaceAll('{', '').replaceAll('}', '').replaceAll('"', '').replaceAll(':', ' - ').replaceAll(',', ', ');
                    $("#output").show();
                    $("#data-output").html("<input type='text' value='" + result + "' name='seq_out' autocomplete='off' />");

                } else if (action == "Protein molar mass") {
                    var arr = sequence.split('');
                    for (var i = 0; i < arr.length; i++) {
                        arr[i] = protein_mass_table[arr[i]];
                    }

                    var result = arr.reduce(function(sum, value) {
                        return sum + value;
                    }, 0);

                    $("#output").show();
                    $("#data-output").html("<ul><li>" + (result - ((arr.length - 1) * water)).toFixed(4) + " g/mole." + "</li></ul>");

                } else if (action == "DNA molar mass" || action == "RNA molar mass") {
                    var arr = sequence.split('');
                    for (var i = 0; i < arr.length; i++) {
                        arr[i] = nucleotide_mass_table[arr[i]];
                    }

                    var result = arr.reduce(function(sum, value) {
                        return sum + value;
                    }, 0);

                    $("#output").show();
                    $("#data-output").html("<ul><li>" + result.toFixed(4) + " g/mole." + "</li></ul>");

                } else if (action == "t-RNA to protein") {
                    var arr = sequence.split('');
                    for (var i = 0; i < arr.length; i++) {
                        arr[i] = rna_complementation[arr[i]];
                    }

                    var m_rna = arr.join('');
                    var result = m_rna.replace(/[AGUC]{3}/g, m => rna_protein_table[m]);
                    $("#output").show();
                    $("#data-output").html("<input type='text' value='" + result + "' name='seq_out' autocomplete='off' />");

                } else if (action == "t-RNA to DNA") {
                    var arr = sequence.split('');
                    for (var i = 0; i < arr.length; i++) {
                        arr[i] = reverse_rna_complementation[arr[i]];
                    }

                    var result = arr.join('');
                    $("#output").show();
                    $("#data-output").html("<input type='text' value='" + result + "' name='seq_out' autocomplete='off' />");

                } else if (action == "m-RNA to DNA") {
                    var result = sequence.replaceAll("U", "T");
                    $("#output").show();
                    $("#data-output").html("<input type='text' value='" + result + "' name='seq_out' autocomplete='off' />");

                } else if (action == "m-RNA to protein") {
                    var result = sequence.replace(/[AGUC]{3}/g, m => rna_protein_table[m]);
                    $("#output").show();
                    $("#data-output").html("<input type='text' value='" + result + "' name='seq_out' autocomplete='off' />");

                } else {
                    $("#output").show();
                    $("#data-output").html("<ul><li>Unable to identify command.</li></ul>");
                }

            } else {
                $("#output").show();
                $("#data-output").html("<ul><li>Invalid input.</li></ul>");
            }
        }

    });
});

String.prototype.replaceAll = function(search, replacement) {
    var target = this;
    return target.split(search).join(replacement);
};
