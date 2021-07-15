import json
import pymysql
import configparser
from datetime import date
import re
from math import ceil

db = configparser.ConfigParser()
db.read('db.ini')
# config.read('/var/www/websites/python/Anuj/finals/db.ini')
host = db['evanik_mainDB']['host']
password = db['evanik_mainDB']['password']
user = db['evanik_mainDB']['user']
db_main = db['evanik_mainDB']['db']
print(host, password, user, db_main)
ratecard = {
    "shippingFee": {
        "2020-11-30": {
            "Small & Standard": {
                "FBA": {
                    "0.0-0.5": {
                        "columns": {
                            "local": {
                                "value": 28
                            },
                            "zonal": {
                                "value": 36
                            },
                            "national": {
                                "value": 56
                            }
                        },
                        "attributes": {
                            "constant": 0
                        }
                    },
                    "0.5-1.0": {
                        "columns": {
                            "local": {
                                "value": 16
                            },
                            "zonal": {
                                "value": 21
                            },
                            "national": {
                                "value": 25
                            }
                        },
                        "attributes": {
                            "constant": 0
                        }
                    },
                    "1.0": {
                        "columns": {
                            "local": {
                                "value": 10
                            },
                            "zonal": {
                                "value": 15
                            },
                            "national": {
                                "value": 20
                            }
                        },
                        "attributes": {
                            "constant": 1
                        }
                    }
                },
                "Seller Flex": {
                    "0.0-0.5": {
                        "columns": {
                            "local": {
                                "value": 28
                            },
                            "zonal": {
                                "value": 36
                            },
                            "national": {
                                "value": 56
                            }
                        },
                        "attributes": {
                            "constant": 0
                        }
                    },
                    "0.5-1.0": {
                        "columns": {
                            "local": {
                                "value": 16
                            },
                            "zonal": {
                                "value": 21
                            },
                            "national": {
                                "value": 25
                            }
                        },
                        "attributes": {
                            "constant": 0
                        }
                    },
                    "1.0": {
                        "columns": {
                            "local": {
                                "value": 10
                            },
                            "zonal": {
                                "value": 15
                            },
                            "national": {
                                "value": 20
                            }
                        },
                        "attributes": {
                            "constant": 1
                        }
                    }
                },
                "Easy Ship": {
                    "0.0-0.5": {
                        "columns": {
                            "local": {
                                "value": 38
                            },
                            "zonal": {
                                "value": 46
                            },
                            "national": {
                                "value": 66
                            }
                        },
                        "attributes": {
                            "constant": 0
                        }
                    },
                    "0.5-1.0": {
                        "columns": {
                            "local": {
                                "value": 16
                            },
                            "zonal": {
                                "value": 21
                            },
                            "national": {
                                "value": 25
                            }
                        },
                        "attributes": {
                            "constant": 0
                        }
                    },
                    "1.0": {
                        "columns": {
                            "local": {
                                "value": 10
                            },
                            "zonal": {
                                "value": 15
                            },
                            "national": {
                                "value": 20
                            }
                        },
                        "attributes": {
                            "constant": 1
                        }
                    }
                }
            },
            "Oversize": {
                "FBA": {
                    "0.0-5.0": {
                        "columns": {
                            "local": {
                                "value": 67
                            },
                            "zonal": {
                                "value": 82
                            },
                            "national": {
                                "value": 132
                            }
                        },
                        "attributes": {
                            "constant": 0
                        }
                    },
                    "5.0": {
                        "columns": {
                            "local": {
                                "value": 10
                            },
                            "zonal": {
                                "value": 11
                            },
                            "national": {
                                "value": 14
                            }
                        },
                        "attributes": {
                            "constant": 1
                        }
                    }
                },
                "Seller Flex": {
                    "0.0-5.0": {
                        "columns": {
                            "local": {
                                "value": 72
                            },
                            "zonal": {
                                "value": 87
                            },
                            "national": {
                                "value": 137
                            }
                        },
                        "attributes": {
                            "constant": 0
                        }
                    },
                    "5.0": {
                        "columns": {
                            "local": {
                                "value": 10
                            },
                            "zonal": {
                                "value": 11
                            },
                            "national": {
                                "value": 14
                            }
                        },
                        "attributes": {
                            "constant": 1
                        }
                    }
                },
                "Easy Ship": {
                    "0.0-5.0": {
                        "columns": {
                            "local": {
                                "value": 101
                            },
                            "zonal": {
                                "value": 116
                            },
                            "national": {
                                "value": 166
                            }
                        },
                        "attributes": {
                            "constant": 0
                        }
                    },
                    "5.0": {
                        "columns": {
                            "local": {
                                "value": 10
                            },
                            "zonal": {
                                "value": 11
                            },
                            "national": {
                                "value": 14
                            }
                        },
                        "attributes": {
                            "constant": 1
                        }
                    }
                }
            },
            "Heavy and Bulky": {
                "FBA": {
                    "0.0-12.0": {
                        "columns": {
                            "local": {
                                "value": 161
                            },
                            "zonal": {
                                "value": 241
                            },
                            "national": {
                                "value": 326
                            }
                        },
                        "attributes": {
                            "constant": 0
                        }
                    },
                    "12.0": {
                        "columns": {
                            "local": {
                                "value": 3
                            },
                            "zonal": {
                                "value": 4
                            },
                            "national": {
                                "value": 10
                            }
                        },
                        "attributes": {
                            "constant": 1
                        }
                    }
                },
                "Seller Flex": {
                    "0.0-12.0": {
                        "columns": {
                            "local": {
                                "value": 166
                            },
                            "zonal": {
                                "value": 246
                            },
                            "national": {
                                "value": None
                            }
                        },
                        "attributes": {
                            "constant": 0
                        }
                    },
                    "12.0": {
                        "columns": {
                            "local": {
                                "value": 3
                            },
                            "zonal": {
                                "value": 4
                            },
                            "national": {
                                "value": None
                            }
                        },
                        "attributes": {
                            "constant": 1
                        }
                    }
                },
                "Easy Ship": {
                    "0.0-12.0": {
                        "columns": {
                            "local": {
                                "value": 166
                            },
                            "zonal": {
                                "value": 246
                            },
                            "national": {
                                "value": None
                            }
                        },
                        "attributes": {
                            "constant": 0
                        }
                    },
                    "12.0": {
                        "columns": {
                            "local": {
                                "value": 3
                            },
                            "zonal": {
                                "value": 4
                            },
                            "national": {
                                "value": None
                            }
                        },
                        "attributes": {
                            "constant": 1
                        }
                    }
                }
            }
        },
        "2020-12-01": {
            "Small & Standard": {
                "FBA": {
                    "0.0-0.5": {
                        "Premium": {
                            "columns": {
                                "local": {
                                    "value": 22
                                },
                                "zonal": {
                                    "value": 36.5
                                },
                                "national": {
                                    "value": 58
                                }
                            },
                            "attributes": {
                                "constant": 0
                            }
                        },
                        "Advanced": {
                            "columns": {
                                "local": {
                                    "value": 22
                                },
                                "zonal": {
                                    "value": 36.5
                                },
                                "national": {
                                    "value": 58
                                }
                            },
                            "attributes": {
                                "constant": 0
                            }
                        },
                        "Standard": {
                            "columns": {
                                "local": {
                                    "value": 28
                                },
                                "zonal": {
                                    "value": 38
                                },
                                "national": {
                                    "value": 59
                                }
                            },
                            "attributes": {
                                "constant": 0
                            }
                        },
                        "Basic": {
                            "columns": {
                                "local": {
                                    "value": 34
                                },
                                "zonal": {
                                    "value": 42.5
                                },
                                "national": {
                                    "value": 63
                                }
                            },
                            "attributes": {
                                "constant": 0
                            }
                        }
                    },
                    "0.5-1.0": {
                        "columns": {
                            "local": {
                                "value": 16
                            },
                            "zonal": {
                                "value": 21
                            },
                            "national": {
                                "value": 26
                            }
                        },
                        "attributes": {
                            "constant": 0
                        }
                    },
                    "1.0-5.0": {
                        "columns": {
                            "local": {
                                "value": 13
                            },
                            "zonal": {
                                "value": 18
                            },
                            "national": {
                                "value": 24
                            }
                        },
                        "attributes": {
                            "constant": 1
                        }
                    },
                    "5.0": {
                        "columns": {
                            "local": {
                                "value": 10
                            },
                            "zonal": {
                                "value": 11
                            },
                            "national": {
                                "value": 15
                            }
                        },
                        "attributes": {
                            "constant": 1
                        }
                    }
                },
                "Seller Flex": {
                    "0.0-0.5": {
                        "Premium": {
                            "columns": {
                                "local": {
                                    "value": 22
                                },
                                "zonal": {
                                    "value": 36.5
                                },
                                "national": {
                                    "value": 58
                                }
                            },
                            "attributes": {
                                "constant": 0
                            }
                        },
                        "Advanced": {
                            "columns": {
                                "local": {
                                    "value": 22
                                },
                                "zonal": {
                                    "value": 36.5
                                },
                                "national": {
                                    "value": 58
                                }
                            },
                            "attributes": {
                                "constant": 0
                            }
                        },
                        "Standard": {
                            "columns": {
                                "local": {
                                    "value": 28
                                },
                                "zonal": {
                                    "value": 38
                                },
                                "national": {
                                    "value": 59
                                }
                            },
                            "attributes": {
                                "constant": 0
                            }
                        },
                        "Basic": {
                            "columns": {
                                "local": {
                                    "value": 34
                                },
                                "zonal": {
                                    "value": 42.5
                                },
                                "national": {
                                    "value": 63
                                }
                            },
                            "attributes": {
                                "constant": 0
                            }
                        }
                    },
                    "0.5-1.0": {
                        "columns": {
                            "local": {
                                "value": 16
                            },
                            "zonal": {
                                "value": 21
                            },
                            "national": {
                                "value": 26
                            }
                        },
                        "attributes": {
                            "constant": 0
                        }
                    },
                    "1.0-5.0": {
                        "columns": {
                            "local": {
                                "value": 13
                            },
                            "zonal": {
                                "value": 18
                            },
                            "national": {
                                "value": 24
                            }
                        },
                        "attributes": {
                            "constant": 1
                        }
                    },
                    "5.0": {
                        "columns": {
                            "local": {
                                "value": 10
                            },
                            "zonal": {
                                "value": 11
                            },
                            "national": {
                                "value": 15
                            }
                        },
                        "attributes": {
                            "constant": 1
                        }
                    }
                },
                "Easy Ship": {
                    "0.0-0.5": {
                        "Premium": {
                            "columns": {
                                "local": {
                                    "value": 32
                                },
                                "zonal": {
                                    "value": 46.5
                                },
                                "national": {
                                    "value": 68
                                }
                            },
                            "attributes": {
                                "constant": 0
                            }
                        },
                        "Advanced": {
                            "columns": {
                                "local": {
                                    "value": 32
                                },
                                "zonal": {
                                    "value": 46.5
                                },
                                "national": {
                                    "value": 68
                                }
                            },
                            "attributes": {
                                "constant": 0
                            }
                        },
                        "Standard": {
                            "columns": {
                                "local": {
                                    "value": 38
                                },
                                "zonal": {
                                    "value": 48
                                },
                                "national": {
                                    "value": 69
                                }
                            },
                            "attributes": {
                                "constant": 0
                            }
                        },
                        "Basic": {
                            "columns": {
                                "local": {
                                    "value": 44
                                },
                                "zonal": {
                                    "value": 52.5
                                },
                                "national": {
                                    "value": 73
                                }
                            },
                            "attributes": {
                                "constant": 0
                            }
                        }
                    },
                    "0.5-1.0": {
                        "columns": {
                            "local": {
                                "value": 16
                            },
                            "zonal": {
                                "value": 21
                            },
                            "national": {
                                "value": 26
                            }
                        },
                        "attributes": {
                            "constant": 0
                        }
                    },
                    "1.0-5.0": {
                        "columns": {
                            "local": {
                                "value": 13
                            },
                            "zonal": {
                                "value": 18
                            },
                            "national": {
                                "value": 24
                            }
                        },
                        "attributes": {
                            "constant": 1
                        }
                    },
                    "5.0": {
                        "columns": {
                            "local": {
                                "value": 10
                            },
                            "zonal": {
                                "value": 11
                            },
                            "national": {
                                "value": 15
                            }
                        },
                        "attributes": {
                            "constant": 1
                        }
                    }
                }
            },
            "Heavy and Bulky": {
                "FBA": {
                    "0.0-12.0": {
                        "Premium": {
                            "columns": {
                                "local": {
                                    "value": 160
                                },
                                "zonal": {
                                    "value": 249.5
                                },
                                "national": {
                                    "value": 325
                                }
                            },
                            "attributes": {
                                "constant": 0
                            }
                        },
                        "Advanced": {
                            "columns": {
                                "local": {
                                    "value": 160
                                },
                                "zonal": {
                                    "value": 249.5
                                },
                                "national": {
                                    "value": 325
                                }
                            },
                            "attributes": {
                                "constant": 0
                            }
                        },
                        "Standard": {
                            "columns": {
                                "local": {
                                    "value": 166
                                },
                                "zonal": {
                                    "value": 251
                                },
                                "national": {
                                    "value": 326
                                }
                            },
                            "attributes": {
                                "constant": 0
                            }
                        },
                        "Basic": {
                            "columns": {
                                "local": {
                                    "value": 172
                                },
                                "zonal": {
                                    "value": 255.5
                                },
                                "national": {
                                    "value": 330
                                }
                            },
                            "attributes": {
                                "constant": 0
                            }
                        }
                    },
                    "12.0": {
                        "columns": {
                            "local": {
                                "value": 4
                            },
                            "zonal": {
                                "value": 5
                            },
                            "national": {
                                "value": 10
                            }
                        },
                        "attributes": {
                            "constant": 1
                        }
                    }
                },
                "Seller Flex": {
                    "0.0-12.0": {
                        "Premium": {
                            "columns": {
                                "local": {
                                    "value": 165
                                },
                                "zonal": {
                                    "value": 254.5
                                },
                                "national": {
                                    "value": 330
                                }
                            },
                            "attributes": {
                                "constant": 0
                            }
                        },
                        "Advanced": {
                            "columns": {
                                "local": {
                                    "value": 165
                                },
                                "zonal": {
                                    "value": 254.5
                                },
                                "national": {
                                    "value": 330
                                }
                            },
                            "attributes": {
                                "constant": 0
                            }
                        },
                        "Standard": {
                            "columns": {
                                "local": {
                                    "value": 171
                                },
                                "zonal": {
                                    "value": 256
                                },
                                "national": {
                                    "value": 331
                                }
                            },
                            "attributes": {
                                "constant": 0
                            }
                        },
                        "Basic": {
                            "columns": {
                                "local": {
                                    "value": 177
                                },
                                "zonal": {
                                    "value": 260.5
                                },
                                "national": {
                                    "value": 335
                                }
                            },
                            "attributes": {
                                "constant": 0
                            }
                        }
                    },
                    "12.0": {
                        "columns": {
                            "local": {
                                "value": 4
                            },
                            "zonal": {
                                "value": 5
                            },
                            "national": {
                                "value": 10
                            }
                        },
                        "attributes": {
                            "constant": 1
                        }
                    }
                },
                "Easy Ship": {
                    "0.0-12.0": {
                        "Premium": {
                            "columns": {
                                "local": {
                                    "value": 175
                                },
                                "zonal": {
                                    "value": 264.5
                                },
                                "national": {
                                    "value": 340
                                }
                            },
                            "attributes": {
                                "constant": 0
                            }
                        },
                        "Advanced": {
                            "columns": {
                                "local": {
                                    "value": 175
                                },
                                "zonal": {
                                    "value": 264.5
                                },
                                "national": {
                                    "value": 340
                                }
                            },
                            "attributes": {
                                "constant": 0
                            }
                        },
                        "Standard": {
                            "columns": {
                                "local": {
                                    "value": 181
                                },
                                "zonal": {
                                    "value": 266
                                },
                                "national": {
                                    "value": 341
                                }
                            },
                            "attributes": {
                                "constant": 0
                            }
                        },
                        "Basic": {
                            "columns": {
                                "local": {
                                    "value": 187
                                },
                                "zonal": {
                                    "value": 270.5
                                },
                                "national": {
                                    "value": 345
                                }
                            },
                            "attributes": {
                                "constant": 0
                            }
                        }
                    },
                    "12.0": {
                        "columns": {
                            "local": {
                                "value": 4
                            },
                            "zonal": {
                                "value": 5
                            },
                            "national": {
                                "value": 10
                            }
                        },
                        "attributes": {
                            "constant": 1
                        }
                    }
                }
            }
        }
    },
    "closingFee": {
        "2020-11-30": {
            "All categories": {
                "FBA": {
                    "1000": {
                        "columns": {
                            "rate": {
                                "value": 26
                            }
                        },
                        "attributes": {}
                    },
                    "501-1000": {
                        "columns": {
                            "rate": {
                                "value": 12
                            }
                        },
                        "attributes": {}
                    },
                    "251-500": {
                        "columns": {
                            "rate": {
                                "value": 20
                            }
                        },
                        "attributes": {}
                    },
                    "0-250": {
                        "columns": {
                            "rate": {
                                "value": 25
                            }
                        },
                        "attributes": {}
                    }
                },
                "Seller Flex": {
                    "1000": {
                        "columns": {
                            "rate": {
                                "value": 43
                            }
                        },
                        "attributes": {}
                    },
                    "501-1000": {
                        "columns": {
                            "rate": {
                                "value": 23
                            }
                        },
                        "attributes": {}
                    },
                    "251-500": {
                        "columns": {
                            "rate": {
                                "value": 8
                            }
                        },
                        "attributes": {}
                    },
                    "0-250": {
                        "columns": {
                            "rate": {
                                "value": 5
                            }
                        },
                        "attributes": {}
                    }
                },
                "Easy Ship": {
                    "1000": {
                        "columns": {
                            "rate": {
                                "value": 50
                            }
                        },
                        "attributes": {}
                    },
                    "501-1000": {
                        "columns": {
                            "rate": {
                                "value": 25
                            }
                        },
                        "attributes": {}
                    },
                    "251-500": {
                        "columns": {
                            "rate": {
                                "value": 5
                            }
                        },
                        "attributes": {}
                    },
                    "0-250": {
                        "columns": {
                            "rate": {
                                "value": 2
                            }
                        },
                        "attributes": {}
                    }
                },
                "Easy Ship Prime": {
                    "1000": {
                        "columns": {
                            "rate": {
                                "value": 43
                            }
                        },
                        "attributes": {}
                    },
                    "501-1000": {
                        "columns": {
                            "rate": {
                                "value": 23
                            }
                        },
                        "attributes": {}
                    },
                    "251-500": {
                        "columns": {
                            "rate": {
                                "value": 8
                            }
                        },
                        "attributes": {}
                    },
                    "0-250": {
                        "columns": {
                            "rate": {
                                "value": 5
                            }
                        },
                        "attributes": {}
                    }
                },
                "MFN": {
                    "1000": {
                        "columns": {
                            "rate": {
                                "value": 59
                            }
                        },
                        "attributes": {}
                    },
                    "501-1000": {
                        "columns": {
                            "rate": {
                                "value": 32
                            }
                        },
                        "attributes": {}
                    },
                    "251-500": {
                        "columns": {
                            "rate": {
                                "value": 16
                            }
                        },
                        "attributes": {}
                    },
                    "0-250": {
                        "columns": {
                            "rate": {
                                "value": 6
                            }
                        },
                        "attributes": {}
                    }
                }
            },
            "Select categories": {
                "FBA": {
                    "1000": {
                        "columns": {
                            "rate": {
                                "value": 26
                            }
                        },
                        "attributes": {}
                    },
                    "501-1000": {
                        "columns": {
                            "rate": {
                                "value": 12
                            }
                        },
                        "attributes": {}
                    },
                    "251-500": {
                        "columns": {
                            "rate": {
                                "value": 20
                            }
                        },
                        "attributes": {}
                    },
                    "0-250": {
                        "columns": {
                            "rate": {
                                "value": 25
                            }
                        },
                        "attributes": {}
                    }
                }
            }
        },
        "2020-12-01": {
            "All categories": {
                "FBA": {
                    "1000": {
                        "columns": {
                            "rate": {
                                "value": 30
                            }
                        },
                        "attributes": {}
                    },
                    "501-1000": {
                        "columns": {
                            "rate": {
                                "value": 15
                            }
                        },
                        "attributes": {}
                    },
                    "251-500": {
                        "columns": {
                            "rate": {
                                "value": 20
                            }
                        },
                        "attributes": {}
                    },
                    "0-250": {
                        "columns": {
                            "rate": {
                                "value": 25
                            }
                        },
                        "attributes": {}
                    }
                },
                "Seller Flex": {
                    "1000": {
                        "columns": {
                            "rate": {
                                "value": 45
                            }
                        },
                        "attributes": {}
                    },
                    "501-1000": {
                        "columns": {
                            "rate": {
                                "value": 25
                            }
                        },
                        "attributes": {}
                    },
                    "251-500": {
                        "columns": {
                            "rate": {
                                "value": 11
                            }
                        },
                        "attributes": {}
                    },
                    "0-250": {
                        "columns": {
                            "rate": {
                                "value": 8
                            }
                        },
                        "attributes": {}
                    }
                },
                "Easy Ship": {
                    "1000": {
                        "columns": {
                            "rate": {
                                "value": 50
                            }
                        },
                        "attributes": {}
                    },
                    "501-1000": {
                        "columns": {
                            "rate": {
                                "value": 28
                            }
                        },
                        "attributes": {}
                    },
                    "251-500": {
                        "columns": {
                            "rate": {
                                "value": 8
                            }
                        },
                        "attributes": {}
                    },
                    "0-250": {
                        "columns": {
                            "rate": {
                                "value": 5
                            }
                        },
                        "attributes": {}
                    }
                },
                "Easy Ship Prime": {
                    "1000": {
                        "columns": {
                            "rate": {
                                "value": 45
                            }
                        },
                        "attributes": {}
                    },
                    "501-1000": {
                        "columns": {
                            "rate": {
                                "value": 25
                            }
                        },
                        "attributes": {}
                    },
                    "251-500": {
                        "columns": {
                            "rate": {
                                "value": 11
                            }
                        },
                        "attributes": {}
                    },
                    "0-250": {
                        "columns": {
                            "rate": {
                                "value": 8
                            }
                        },
                        "attributes": {}
                    }
                },
                "MFN": {
                    "1000": {
                        "columns": {
                            "rate": {
                                "value": 59
                            }
                        },
                        "attributes": {}
                    },
                    "501-1000": {
                        "columns": {
                            "rate": {
                                "value": 32
                            }
                        },
                        "attributes": {}
                    },
                    "251-500": {
                        "columns": {
                            "rate": {
                                "value": 16
                            }
                        },
                        "attributes": {}
                    },
                    "0-250": {
                        "columns": {
                            "rate": {
                                "value": 6
                            }
                        },
                        "attributes": {}
                    }
                }
            },
            "Select categories": {
                "FBA": {
                    "1000": {
                        "columns": {
                            "rate": {
                                "value": 30
                            }
                        },
                        "attributes": {}
                    },
                    "501-1000": {
                        "columns": {
                            "rate": {
                                "value": 15
                            }
                        },
                        "attributes": {}
                    },
                    "251-500": {
                        "columns": {
                            "rate": {
                                "value": 12
                            }
                        },
                        "attributes": {}
                    },
                    "0-250": {
                        "columns": {
                            "rate": {
                                "value": 25
                            }
                        },
                        "attributes": {}
                    }
                }
            }
        }
    },
    "pickAndPackFee": {
        "2020-11-30": {
            "Small": {
                "columns": {
                    "value": 10
                }
            },
            "Standard": {
                "columns": {
                    "value": 10
                }
            },
            "Oversize": {
                "columns": {
                    "value": 25
                }
            },
            "HB": {
                "columns": {
                    "value": 50
                }
            }
        },
        "2020-12-01": {
            "Standard": {
                "columns": {
                    "value": 10
                }
            },
            "HB": {
                "columns": {
                    "value": 50
                }
            }
        }
    },
    "disposalFee": {
        "2020-11-30": {
            "Small": {
                "columns": {
                    "value": 5
                }
            },
            "Standard": {
                "columns": {
                    "value": 10
                }
            },
            "Oversize": {
                "columns": {
                    "value": 25
                }
            },
            "HB": {
                "columns": {
                    "value": 25
                }
            }
        },
        "2020-12-01": {
            "Standard": {
                "columns": {
                    "value": 0
                }
            },
            "HB": {
                "columns": {
                    "value": 0
                }
            }
        }
    },
    "removalFee": {
        "Self Pickup/Standard shipping": {
            "2020-11-30": {
                "Small": {
                    "columns": {
                        "value": 5
                    }
                },
                "Standard": {
                    "columns": {
                        "value": 10
                    }
                },
                "Oversize": {
                    "columns": {
                        "value": 25
                    }
                },
                "HB": {
                    "columns": {
                        "value": 25
                    }
                }
            },
            "2020-12-01": {
                "Standard": {
                    "columns": {
                        "value": 10
                    }
                },
                "HB": {
                    "columns": {
                        "value": 100
                    }
                }
            }
        },
        "Expedited shipping": {
            "2020-11-30": {
                "Small": {
                    "columns": {
                        "value": 15
                    }
                },
                "Standard": {
                    "columns": {
                        "value": 30
                    }
                },
                "Oversize": {
                    "columns": {
                        "value": 50
                    }
                },
                "HB": {
                    "columns": {
                        "value": 50
                    }
                }
            },
            "2020-12-01": {
                "Standard": {
                    "columns": {
                        "value": 30
                    }
                },
                "HB": {
                    "columns": {
                        "value": 300
                    }
                }
            }
        }
    },
    "lightningDealFee": {
        "2020-11-30": {
            "Premium": {
                "columns": {
                    "value": 149
                }
            },
            "Advanced": {
                "columns": {
                    "value": 149
                }
            },
            "Standard": {
                "columns": {
                    "value": 149
                }
            },
            "Basic": {
                "columns": {
                    "value": 149
                }
            }
        },
        "2020-12-01": {
            "Premium": {
                "columns": {
                    "value": 133
                }
            },
            "Advanced": {
                "columns": {
                    "value": 133
                }
            },
            "Standard": {
                "columns": {
                    "value": 149
                }
            },
            "Basic": {
                "columns": {
                    "value": 166
                }
            }
        }
    }
}


def get_data(db_user, start_date, end_date):
    print('hello')

    print(db_user, start_date, end_date)
    connection2 = pymysql.connect(host=host, user=user, password=password, database=db_user)
    cursor2 = connection2.cursor()
    query = f"""
			SELECT
        s.OrderId,
        s.OrderItemID,
        s.sale_status,
        s.payment_status,
        SUM(s.grand_total) AS grand_total,
        SUM(DISTINCT pp.fixed_fee),
        s.sellerId,
        s.whid,
        s.invoice_number,
        s.date,
        s.total_items AS total_items,
        s.staff_note,
        s.PinCode AS To_pincode,
        c.pincode AS From_pincode,
        s.shippingZone,
        s.weight,
        s.shipmentLength,
        s.shipmentBreadth,
        s.shipmentHeight,
        pr.length,
        pr.breadth,
        pr.height,
        pr.weight,
        pp.extra_details 
    FROM
        sales AS s 
    JOIN
        payments_process AS pp 
            ON (
                s.OrderId = pp.OrderId 
                AND (
                    (
                        pp.SKUCode LIKE REPLACE(s.SKUCode,
                    ' ',
                    '%') 
                    OR s.SKUCode LIKE REPLACE(pp.SKUCode,
                    ' ',
                    '%') 
                    OR pp.SKUCode LIKE REPLACE(s.SKUCode,
                    '_',
                    '%')))) 
                JOIN
                    channels AS c 
                        ON (
                            c.sellerId = s.sellerId
                        ) 
                JOIN
                    products AS pr 
                        ON (
                            pr.code = s.SKUcode 
                            AND pr.seller_Id = s.sellerId
                        ) 
                WHERE
                    c.type = 'amazon' 
                    AND s.sale_status = 'Shipped' 
                    AND (
                        s.date BETWEEN '{start_date}' AND '{end_date}'
                    ) 
                    AND s.OrderId = '406-4836749-3400349' 
                GROUP BY
                    s.OrderId,
                    s.SKUCode 
                ORDER BY
                    NULL
			"""

    cursor2.execute(query)
    data = cursor2.fetchall()
    print(data)
    cursor2.close()
    connection2.close()
    # and s.OrderId='171-0061230-2648300'
    #  limit 3000
    return data


def get_tier(db_user):
    connection2 = pymysql.connect(host=host, user=user, password=password, database=db_user)
    cursor2 = connection2.cursor()
    query = """
			SELECT ct.sellerId, ct.tier, ct.start_date, ct.end_date FROM channel_tiers AS ct
			JOIN channels AS ch ON ch.sellerId=ct.sellerId
			WHERE ch.type='amazon'
			"""
    cursor2.execute(query)
    tier_data = cursor2.fetchall()
    cursor2.close()
    connection2.close()
    return tier_data


def get_state(to_pin, from_pin):
    while True:
        try:
            connection_evanik_main = pymysql.connect(host=host, user=user, password=password, database=db_main)
            cursor_evanik_main = connection_evanik_main.cursor()

            query_to = f"Select flipkart_region,District, statename from pincodes where pincode={to_pin}"
            query_from = f"Select flipkart_region, District, statename from pincodes where pincode={from_pin}"
            cursor_evanik_main.execute(query_to)
            data_to = cursor_evanik_main.fetchone()
            cursor_evanik_main.execute(query_from)
            data_from = cursor_evanik_main.fetchone()

            from_fk_region = data_from[0]
            from_district = data_from[1]
            from_state = data_from[2]

            to_fk_region = data_to[0]
            to_district = data_to[1]
            to_state = data_to[2]

            if to_district == from_district:
                applicable_zone = 'local'
            elif (to_district != from_district) and (to_fk_region == from_fk_region):
                # applicable_zone = 'Zonal'
                applicable_zone = 'zonal'
            else:
                applicable_zone = 'national'

            cursor_evanik_main.close()
            connection_evanik_main.close()
        except pymysql.OperationalError:
            connection_evanik_main = pymysql.connect(host=host, user=user, password=password, database=db_main)
            cursor_evanik_main = connection_evanik_main.cursor()
            continue
        except:
            print('state not found')
            applicable_zone = None
            break
        else:
            print('state found')
        return applicable_zone


def calculate_closingFee(dated, category, type, grand_total, total_items):
    item_price = grand_total / total_items
    li = [i for i in ratecard['closingFee'][dated][category][type]]
    for j in li:
        if j.__contains__('-'):
            first = float(j.split('-')[0])
            last = float(j.split('-')[1])
            if item_price > first and item_price <= last:
                applicable_closing = ratecard['closingFee'][dated][category][type][j]['columns']['rate']['value']
        else:
            if item_price > float(j):
                applicable_closing = ratecard['closingFee'][dated][category][type][j]['columns']['rate']['value']
    applicable_closing = float(applicable_closing) * float(total_items)
    # print(f'applicable_closing: {applicable_closing}')
    return applicable_closing


def calculate_shippingFee(dated, sizeband, type, step, applicable_zone, applicable_weight, total_items):
    slabs = [i for i in ratecard["shippingFee"][dated][sizeband][type].keys() if
             float(i.split('-')[0]) < applicable_weight]
    print(slabs)
    applicable_shipping = 0
    for slab in slabs:
        # constant = ratecard["shippingFee"][dated][sizeband][type][slab][step]['attributes']['constant']
        if (slab == '0.0-0.5') or (slab == '0.0-12.0'):
            constant = ratecard["shippingFee"][dated][sizeband][type][slab][step]['attributes']['constant']
            fee = ratecard["shippingFee"][dated][sizeband][type][slab][step]['columns'][applicable_zone]['value']
        else:
            constant = ratecard["shippingFee"][dated][sizeband][type][slab]['attributes']['constant']
            fee = ratecard["shippingFee"][dated][sizeband][type][slab]['columns'][applicable_zone]['value']
        print(f'constant: {constant}, fee: {fee}')
        if slab.__contains__('-'):
            first, last = float(slab.split('-')[0]), float(slab.split('-')[1])
            print(f'first: {first}, last:{last}')
            if last <= applicable_weight:
                difference = last - first
                print(f'difference: {difference}')
            else:
                print(f"applicable_weight: {applicable_weight} , first: {first}")
                difference = applicable_weight
                print(f'difference: {difference}')
            try:
                rep = ceil(difference / constant)
                print(f'rep: {rep}')
            except ZeroDivisionError as e:
                applicable_shipping += fee
                print(applicable_shipping)
                applicable_weight -= float(difference)
                print(f'applicable_weight: {applicable_weight}')
                continue
            except Exception as e:
                pass
            else:
                applicable_shipping += (fee * rep)
                print(applicable_shipping)
                applicable_weight -= (rep * constant)
                print(f'applicable_weight: {applicable_weight}')
        if not slab.__contains__('-'):
            rep = applicable_weight / constant
            applicable_shipping += (fee * rep)
            print(applicable_shipping)
            applicable_weight -= (rep * constant)
            print(f'applicable_shipping = {applicable_shipping}')

    applicable_shipping = applicable_shipping * float(total_items)
    print(f'applicable_shipping: {applicable_shipping}')
    return applicable_shipping


def calculate_pickpack(dated, applicable_weight, total_items):
    # dated = '2020-12-01'
    if applicable_weight >= 12:
        sizeband = 'HB'
    else:
        sizeband = 'Standard'
    applicable_pickpack = float(ratecard["pickAndPackFee"][dated][sizeband]["columns"]["value"]) * float(total_items)
    return applicable_pickpack


def calculate_techfee(total_items):
    applicable_techfee = float(10) * float(total_items)
    return applicable_techfee


def insert_data(db_user, val):
    query = """
					INSERT INTO charges_shipping_variance (marketplace, `channel`, warehouse, order_id, item_id,
					sale_status, payment_status, order_date, grand_total, extra_1, reco_head)
					VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
					ON DUPLICATE KEY UPDATE marketplace = %s, `channel` = %s, warehouse = %s, order_id = %s,
					item_id = %s, sale_status = %s, payment_status = %s, order_date = %s, grand_total = %s, extra_1 = %s, reco_head = %s
				"""

    try:
        connection = pymysql.connect(host=host, user=user, password=password, database=db_user)
        cursor = connection.cursor()

        cursor.execute(query, val)
        connection.commit()
        print(cursor.rowcount, "record inserted.")

        cursor.close()
        connection.close()
    except pymysql.OperationalError:
        print('pymysql.OperationalError')
        connection = pymysql.connect(host=host, user=user, password=password, database=db_user)
        cursor = connection.cursor()

        cursor.execute(query, val)
        connection.commit()
        print(cursor.rowcount, "record inserted.")
        cursor.close()
        connection.close()


def main(userid, start_date, end_date):
    db_user = db['invento_useridDB']['db']
    db_user = db_user.format(userid)
    g = ['SVGA', 'SGAB', 'SPAB', 'SDED', 'SDEE', 'SDEF', 'AMD1', 'SAMD', 'XWAE', 'DEL2', 'DEL4', 'DEL5', 'DED3', 'SDEG',
         'SDEI', 'XNAB', 'BLR5', 'BLR7', 'SBLG', 'XSAJ', 'BOM1', 'BOM3', 'BOM4', 'BOM5', 'BOM6', 'BOM7', 'NAG1', 'SBOA',
         'SBOC', 'SBOK', 'SPNA', 'SPNC', 'XWAA', 'SBHA', 'SIDA', 'SATA', 'SATB', 'SJAB', 'HYD8', 'HYD3', 'SHYB', 'XSAD',
         'MAA4', 'MAA5', 'SCJA', 'SCJB', 'SMAB', 'SMAB', 'SLKA', 'SLKB', 'SCCC', 'SCCE', 'SCCF', 'SCCG', 'SCCH', 'XEAA']
    datas = get_data(db_user, start_date, end_date)
    tier_data = get_tier(db_user)

    for i in datas:
        orderid, orderitemid, sale_status, payment_status, grand_total, fixed_fee, sellerid, warehouse, invoice_number, \
        order_date, total_items, staff_note, to_pincode, from_pincode, appliedshippingzone, applied_weight, \
        applied_Length, applied_Breadth, applied_Height, length, breadth, height, weight, extra_details \
            = i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], \
              i[16], i[17], i[18], i[19], i[20], i[21], i[22], i[23]
        # print(orderid, orderitemid, sale_status, payment_status, grand_total, fixed_fee, sellerid, whid, invoice_number,order_date, total_items, staff_note, to_pincode, from_pincode, appliedshippingzone, applied_weight, applied_Length, applied_Breadth, applied_Height, length, breadth, height, weight, extra_details)
        print(f'orderid:{orderid}, orderitemid:{orderitemid}, invoice_number:{invoice_number}')
        # applied
        print(f'applied_Length: {applied_Length}, applied_Height: {applied_Height}, applied_Breadth: {applied_Breadth}')

        if (applied_Length is not None) and (applied_Height is not None) and (applied_Breadth is not None):
            calc_applied_weight = (float(applied_Height) * float(applied_Length) * float(applied_Breadth)) / 5000
            if applied_weight is not None:
                applied_weight = max(float(applied_weight), calc_applied_weight)
            else:
                applied_weight = calc_applied_weight
        elif applied_weight is not None:
            applied_weight = float(applied_weight)
        else:
            applied_weight = None
        print(f'applied_weight: {applied_weight}')
        print(f'appliedshippingzone: {appliedshippingzone}')
        try:
            applied_shippingfee = abs(float(extra_details.split('"FBA Weight Handling Fee";d:')[1].split(";")[0]))
        except IndexError:  # "Easy Ship weight handling fees";s:6:"-68.00";
            try:
                applied_shippingfee = abs(
                    float(extra_details.split('"Easy Ship weight handling fees";s:')[1].split('"')[1]))
            except IndexError:
                applied_shippingfee = 0
        finally:
            print(f'applied_shippingfee: {applied_shippingfee}')
        # applied_commission = abs(float(extra_details.split('"Commission";d:')[1].split(";")[0]))
        # print(f'applied_commission: {applied_commission}')
        try:
            applied_closingfee = abs(float(extra_details.split('"Fixed closing fee";d:')[1].split(";")[0]))
        except IndexError:
            applied_closingfee = 0
        print(f'applied_closingfee: {applied_closingfee}')
        # applied_shippingchargeback = abs(float(extra_details.split('"Shipping Chargeback";d:')[1].split(";")[0]))

        # applicable fee components
        if (length is not None) and (height is not None) and (breadth is not None):
            calc_applicable_weight = (float(height) * float(length) * float(breadth)) / 5000
            if weight is not None:
                applicable_weight = max(float(weight), calc_applicable_weight)
            else:
                applicable_weight = calc_applicable_weight
        elif weight is not None:
            applicable_weight = float(weight)
        else:
            applicable_weight = None
        applicable_zone = get_state(to_pincode, from_pincode)

        if order_date <= date(2020, 11, 30):
            dated = "2020-11-30"
        else:
            dated = "2020-12-01"
        category = "All categories"
        try:
            if ((re.match(r"IN-[0-9A-Z]{4,5}-[0-9]{1,7}", invoice_number)) or (
                    re.match(r"[0-9A-Z]{4,5}-[0-9]{1,7}", invoice_number))) and str(invoice_number).strip() is not None:
                if (invoice_number[3:7] in g) or (invoice_number[0:4] in g):  # fba
                    type = 'FBA'
                elif (invoice_number[3:7] not in g) or (invoice_number[0:4] not in g):  # seller flex
                    type = 'Seller Flex'
            else:
                if ((warehouse is None) or (warehouse == '')) and (staff_note == 'Easy Ship'):  # 'Easy Ship'
                    type = 'Easy Ship'
                elif ((warehouse is None) or (warehouse == '')) and (staff_note != 'Easy Ship'):  # "Self Ship"
                    type = 'Easy Ship Prime'
                else:
                    type = 'MFN'
        except:
            continue
        if applicable_weight >= 22.5:
            sizeband = 'Heavy and Bulky'
        else:
            sizeband = 'Small & Standard'
        step = 'Standard'

        print(f'dated: {dated}, category: {category}, type: {type}, applicable_zone: {applicable_zone}, '
              f'applicable_weight: {applicable_weight}, sizeband: {sizeband}, step: {step}, grand_total: {grand_total}, quantity:{total_items}')

        # def calculate_shippingFee():
        try:
            applicable_closing = calculate_closingFee(dated, category, type, grand_total, total_items)
            print(f'applicable_closing: {applicable_closing}')
        except UnboundLocalError:
            print(f'{orderid} skip due to applicable closing fee not found')
        try:
            applicable_shipping = calculate_shippingFee(dated, sizeband, type, step, applicable_zone, applicable_weight,
                                                        total_items)
            print(f'applicable_shipping: {applicable_shipping}')
        except:
            print(f'{orderid} skip due to applicable shipping fee not found')
        if type == 'FBA':
            try:
                applied_pickpackfee = abs(float(extra_details.split('"FBA Pick & Pack Fee";d:')[1].split(";")[0]))
            except IndexError:
                applied_pickpackfee = 0
            applicable_pickpack = calculate_pickpack(dated, applicable_weight, total_items)
            print(f'applied_pickpackfee: {applied_pickpackfee}, applicable_pickpack: {applicable_pickpack}')
            extra_1 = {
                "Closing Fee": {"Applied Fee": applied_closingfee, "Applicable Fee": applicable_closing,
                                "Gap": applied_closingfee - applicable_closing},
                "Pick & Pack Fee": {"Applied Fee": applied_pickpackfee, "Applicable Fee": applicable_pickpack,
                                    "Gap": applied_pickpackfee - applicable_pickpack},
                "Shipping Fee": {"Applied Fee": applied_shippingfee, "Applicable Fee": applicable_shipping,
                                 "Applied Weight": applied_weight, "Applicable Weight": applicable_weight,
                                 "Applied Zone": appliedshippingzone, "Applicable Zone": applicable_zone,
                                 "Gap": applied_shippingfee - applicable_shipping},
            }
        else:
            try:
                applied_techfee = abs(float(extra_details.split('"Technology Fee";d:')[1].split(";")[0]))
            except IndexError:
                applied_techfee = 0
            print(f'applied_techfee: {applied_techfee}')
            applicable_techfee = calculate_techfee(total_items)
            print(f'applicable_techfee: {applicable_techfee}')
            extra_1 = {
                "Closing Fee": {"Applied Fee": applied_closingfee, "Applicable Fee": applicable_closing,
                                "Gap": applied_closingfee - applicable_closing},
                "Shipping Fee": {"Applied Fee": applied_shippingfee, "Applicable Fee": applicable_shipping,
                                 "Applied Weight": applied_weight, "Applicable Weight": applicable_weight,
                                 "Applied Zone": appliedshippingzone, "Applicable Zone": applicable_zone,
                                 "Gap": applied_shippingfee - applicable_shipping},
                "Technology Fee": {"Applied Fee": applied_techfee, "Applicable Fee": applicable_techfee,
                                   "Gap": applied_techfee - applicable_techfee}
            }
        marketplace = 'amazon'
        reco_head = "amazon_all"
        val = (
            marketplace, sellerid, warehouse, orderid, orderitemid, sale_status, payment_status, order_date,
            grand_total,
            json.dumps(extra_1), reco_head,
            marketplace, sellerid, warehouse, orderid, orderitemid, sale_status, payment_status, order_date,
            grand_total,
            json.dumps(extra_1), reco_head
        )
        print(val)
        insert_data(db_user, val)


if __name__ == '__main__':
    userid = 76137
    start_date = date(2021, 5, 1)
    end_date = date(2021, 5, 31)
    main(userid, start_date, end_date)
