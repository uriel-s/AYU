<?php



require_once("$CFG->libdir/formslib.php");

class edit extends moodleform {
    public function definition() {
        $mform = $this->_form; // Don't forget the unders core!
        global $CFG;

        $mform->addElement('text', 'git_url', ' קישור לבדקן'); // Add elements to your form
        $mform->setType('git_url', PARAM_NOTAGS);                   //Set type of element
        $mform->setDefault('git_url', 'Please enter the Github url');        //Default value
        

        $mform->addElement('text', 'user_name', ' שם'); // Add elements to your form
        $mform->setType('user_name', PARAM_NOTAGS);                   //Set type of element
        $mform->setDefault('user_name', ' enter yout full name');        //Default value

        
       
        $this->add_action_buttons();
    }


    function validation($data, $files) {
        return array();
    }
}