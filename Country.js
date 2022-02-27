const mongoose = require('mongoose');

const CountryModel = mongoose.model('Country', {
    name: {
        type: String,
        required: true,
        unique: true
    },
    isoCode: {
        type: String
    },
    //##2
    continent: [{
        type: mongoose.Schema.Types.ObjectId,
        ref: "Continent"
    }],
    //##5
    population: {
        type: Number,
        default: -1
    },
});

module.exports = CountryModel