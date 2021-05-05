<?php



require_once("$CFG->libdir/formslib.php");

class edit extends moodleform {
    public function definition() {
        $mform = $this->_form; // Don't forget the unders core!
        global $CFG;

        $mform->addElement('text', 'github_url', ' קישור לבדקן'); // Add elements to your form
        $mform->setType('github_url', PARAM_NOTAGS);                   //Set type of element
        $mform->setDefault('github_url', 'Please enter the Github url');        //Default value
        

        // $mform->addElement('text', 'id_', ' תעודת זהות'); // Add elements to your form
        // $mform->setType('id_', PARAM_NOTAGS);                   //Set type of element
        // $mform->setDefault('id_', 'הכנס ת.ז');        //Default value



        $mform->addElement('text', 'name_', ' שם'); // Add elements to your form
        $mform->setType('id_', PARAM_NOTAGS);                   //Set type of element
        $mform->setDefault('name_', ' enter yout full name');        //Default value

        
       
        $this->add_action_buttons();
    }


    function validation($data, $files) {
        return array();
    }
}