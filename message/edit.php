<?php

require_once(__DIR__ . '/../../config.php');
require_once($CFG->dirroot . '/local/message/classes/form/edit.php');
global $DB;
$PAGE->set_url(new moodle_url('/local/message/edit.php'));
$PAGE->set_context(\context_system::instance());
$PAGE->set_title('Edit');


// We want to display our form.
$mform = new edit();

if ($mform->is_cancelled()) {
    // Go back to manage.php page
    redirect($CFG->wwwroot . '/local/message/manage.php', 'העלאת הקישור לבדקן בוטלה',$type = \core\output\notification::NOTIFY_WARNING);
}

else if ($fromform = $mform->get_data()) {

    // Insert the data into our database table.
    $recordtoinsert = new stdClass();
    $recordtoinsert->github_url = $fromform->github_url;
    $recordtoinsert->id_ = $fromform->id_;
    $recordtoinsert->name_ = $fromform->name_;

    $DB->insert_record('local_message', $recordtoinsert);
    redirect($CFG->wwwroot . '/local/message/manage.php', 'send   :' . $fromform->github_url. '  to Badkan');

}

echo $OUTPUT->header();
echo'just e ';
$mform->display();
echo $OUTPUT->footer();